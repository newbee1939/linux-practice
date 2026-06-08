#!/usr/bin/python3

while True:
    pass


# ❯ docker run --platform linux/arm64 -it --rm \
#   --cap-add=SYS_PTRACE \
#   --security-opt seccomp=unconfined \
#   linux-practice-arm64
# root@6cb2784402@ac:/work# ls
# hello  hello.go  hello.py  inf-loop.py
# root@6cb2784402@ac:/work# taskset -c 0 ./inf-loop.py &
# [1] 14
# root@6cb2784402@ac:/work# sar -P 0 1 1
# Linux 6.10.14-linuxkit (6cb2784402@ac)   06/08/26        _aarch64_       (10 CPU)

# 09:32:39        CPU     %user     %nice   %system   %iowait    %steal     %idle
# 09:32:40          0    100.00      0.00      0.00      0.00      0.00      0.00
# Average:          0    100.00      0.00      0.00      0.00      0.00      0.00
