#!/bin/sh
set -eu
cd "$(dirname "$0")"
PYTHONOPTIMIZE=0 python3 current/low/verify.py
PYTHONOPTIMIZE=0 python3 current/low/check_data.py
PYTHONOPTIMIZE=0 python3 current/near/verify_near.py
PYTHONOPTIMIZE=0 python3 current/middle_high/verify_middle_high.py
