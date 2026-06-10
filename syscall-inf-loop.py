#!/usr/bin/python3

import os

while True:
    os.getpid()

# taskset -c 0 ./syscall-inf-loop.py &
# sar -P 0 1 1
