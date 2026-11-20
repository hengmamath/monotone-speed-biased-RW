"""Rebuild the complete exact certificate package for the scoped theorem.

Uses existing Python/Sympy; installs nothing. The older >=707/500 proof
module is independently audited and linked in the manuscript. No original
user note, credentials or external service is touched.
"""
from pathlib import Path
import subprocess
import sys
base=Path(__file__).resolve().parent
scripts=(
 'assigned_polynomial_extension.py',
 'root_canonical_profile_payment.py',
 'condition_F_joint_prefix_identities.py',
 'condition_F_global_gram_certificate.py',
 'root_four_term_original_identities.py',
 'root_four_small_u_certificate.py',
 'high_u_original_root_s2_identities.py',
 'high_u_original_root_s2.py',
)
for name in scripts:
 print('Rebuilding exact module:',name,flush=True)
 subprocess.run([sys.executable,str(base/name)],cwd=base,check=True)
print('All exact scoped-theorem certificate modules completed.',flush=True)
