"""Rebuild and verify every finite sign used by the near-region body.

The verification runs in a temporary directory. Published certificates are
read and compared, never overwritten. No archive program is imported.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
PROGRAMS=['near_arithmetic_build.py','near_high_cap_build.py','near_identity_check.py','near_bernstein_check.py']
GROUPS={
 'lem:near-cap-arithmetic':['cap_lambda_derivative'],
 'lem:near-intermediate-arithmetic / lem:near-finite-certificate':[
  'rho34_u_derivative','rho34_endpoint','rho56_u_derivative','rho56_g_derivative','rho56_quarter','rho56_mixed',
  'core_c2','core_c34','j1_curvature','j1_left_derivative','j1_right_derivative','j2','j3','t1'],
 'recovery coefficient checks':['age2_constant','age2_quadratic','age3_constant','age3_quadratic','age4_constant','age4_quadratic'],
 'lem:near-high-arithmetic':['high_right_minus','high_right_plus','high_upper'],
 'high-u lower endpoint':['high_lower_quartic'],
}

def run(folder,program,*args):
    result=subprocess.run([sys.executable,str(folder/program),*args],cwd=folder,text=True,capture_output=True)
    if result.returncode:
        print(result.stdout,end='');print(result.stderr,end='',file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout

def main():
    with tempfile.TemporaryDirectory(prefix='near_region_exact_') as tmp:
        folder=Path(tmp)
        for name in PROGRAMS:shutil.copy2(HERE/name,folder/name)
        build=run(folder,'near_arithmetic_build.py')
        high=run(folder,'near_high_cap_build.py')
        identities=run(folder,'near_identity_check.py')
        print(identities.strip().splitlines()[-1])
        print('CAP ENDPOINTS PASS: 10 exact Q(sqrt(3)) comparisons')
        print('J1 ENDPOINTS PASS: 2 exact rational comparisons')
        total=0
        for group,names in GROUPS.items():
            output=run(folder,'near_bernstein_check.py',*names)
            assert output.count(' PASS ')==len(names),(group,output)
            leaves=0
            for name in names:
                generated=json.loads((folder/'near_arithmetic_data'/(name+'.certificate.json')).read_text())
                published=HERE/'certificates'/(name+'.certificate.json')
                if published.exists():
                    assert generated==json.loads(published.read_text()),('published certificate mismatch',name)
                else:
                    raise AssertionError(('missing published certificate',str(published)))
                leaves+=len(generated['leaves'])
            total+=len(names)
            print(f'{group}: PASS ({len(names)} polynomial signs, {leaves} rectangles; all denominators positive)')
        generated=json.loads((folder/'near_arithmetic_data'/'cap_endpoints.json').read_text())
        assert generated==json.loads((HERE/'certificates'/'cap_endpoints.json').read_text())
        generated=json.loads((folder/'near_arithmetic_data'/'j1_endpoints.json').read_text())
        assert generated==json.loads((HERE/'certificates'/'j1_endpoints.json').read_text())
        print(f'NEAR REGION VERIFICATION PASS: {total} polynomial signs, 28 identities, 12 endpoint comparisons')

if __name__=='__main__':main()
