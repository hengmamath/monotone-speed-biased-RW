"""Rerun the exact finite certificate modules of the final modular proof.

No installation, network, credentials, git, or mathematical sampling.
The manifest and referenced manual proofs are required alongside this entry.
Default: list; --check: validate reviewed file hashes; --run GROUP: rerun.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent
MANIFEST = BASE / "final_certificate_manifest_20261004.json"


def certificate_environment():
    # Certificate programs use assert; these guards must not use assert.
    if not __debug__:
        raise RuntimeError("Certificate replay requires assertions: do not use -O or -OO.")
    if sys.flags.optimize != 0:
        raise RuntimeError("Certificate replay requires sys.flags.optimize == 0.")
    if os.environ.get("PYTHONOPTIMIZE") not in (None, "", "0"):
        raise RuntimeError("Certificate replay rejects enabled PYTHONOPTIMIZE; unset it.")
    child_env = os.environ.copy()
    child_env.pop("PYTHONOPTIMIZE", None)
    return child_env


def check_child_interpreter(child_env):
    probe = (
        "import os,sys; "
        "bad=(not __debug__) or sys.flags.optimize!=0 or 'PYTHONOPTIMIZE' in os.environ; "
        "print('Child interpreter: optimize='+str(sys.flags.optimize)"
        "+'; __debug__='+str(__debug__)+'; PYTHONOPTIMIZE_present='"
        "+str('PYTHONOPTIMIZE' in os.environ),flush=True); "
        "\nif bad: raise RuntimeError('Child interpreter must preserve assertions')\n"
    )
    subprocess.run([sys.executable, "-c", probe], env=child_env, check=True)


def read_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def check_files(manifest):
    failures = []
    for record in manifest["reviewed_files"]:
        path = BASE / record["path"]
        if not path.is_file():
            failures.append(record["path"] + ": missing")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            failures.append(record["path"] + ": hash mismatch")
    if failures:
        raise SystemExit("Manifest check FAILED:\n" + "\n".join(failures))
    print(f"Manifest integrity PASS: {len(manifest['reviewed_files'])} files.")


def main():
    child_env = certificate_environment()
    print("Execution guard: runner optimize=0; __debug__=True; child PYTHONOPTIMIZE removed.", flush=True)
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--check", action="store_true")
    actions.add_argument("--run", metavar="GROUP")
    args = parser.parse_args()
    manifest = read_manifest()
    groups = {item["id"]: item for item in manifest["groups"]}
    if args.check:
        check_files(manifest)
        return
    if args.run is None:
        print(manifest["proof_status"])
        print("Finite computations accompany the manual proofs; external probability inputs are imported.")
        for group in groups.values():
            print(f"{group['id']}: {group['scope']}")
            for name in group["scripts"]:
                print("  " + name)
        print("Use --check, --run GROUP, or --run all. Full replay can be lengthy.")
        return
    if args.run != "all" and args.run not in groups:
        raise SystemExit("Unknown group: " + args.run)
    check_files(manifest)
    check_child_interpreter(child_env)
    chosen = list(groups.values()) if args.run == "all" else [groups[args.run]]
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    log_dir = BASE / "final_certificate_replays" / timestamp
    log_dir.mkdir(parents=True, exist_ok=False)
    scripts = list(dict.fromkeys(name for group in chosen for name in group["scripts"]))
    print("Replay log directory: " + str(log_dir), flush=True)
    print("Historical pending/open print labels are superseded by dated receipts.", flush=True)
    for index, name in enumerate(scripts, 1):
        log = log_dir / (f"{index:02d}_" + Path(name).stem + ".txt")
        print(f"Running {index}/{len(scripts)}: {name}", flush=True)
        with log.open("w", encoding="utf-8") as stream:
            result = subprocess.run(
                [sys.executable, str(BASE / name)],
                cwd=BASE, stdout=stream, stderr=subprocess.STDOUT,
                env=child_env, check=False)
        if result.returncode != 0:
            print(log.read_text(encoding="utf-8")[-8000:], file=sys.stderr)
            raise SystemExit(f"FAILED exit={result.returncode}: {name}; log={log}")
        print("PASS exit=0; log=" + str(log), flush=True)
    print("Requested exact modules all exited zero.")
    print("This does not replace manual tail, response, scope or probability proofs.")


if __name__ == "__main__":
    main()
