#!/usr/bin/python3

import os, sys

# os.fork() は「呼び出したプロセスを複製」してプロセスを2つに分裂させるシステムコール。
# この1行を境に、親プロセスと子プロセスの「2つ」がそれぞれ別々に以降の行を実行していく。
#
# 重要なのは os.fork() の戻り値が、親と子で「異なる」こと:
#   - 親プロセス側  : 生成された子プロセスの PID（正の整数）が返る
#   - 子プロセス側  : 0 が返る
# この戻り値の違いを使って「今自分は親なのか子なのか」を if 文で振り分ける。
ret = os.fork()

if ret == 0:
    # ret == 0 → 自分は「子プロセス」。この print は子プロセスだけが実行する。
    # os.getpid()  : 自分自身の PID
    # os.getppid() : 親プロセスの PID（= fork した親の PID になる）
    print("子プロセス: pid={}, ppid={}".format(os.getpid(), os.getppid()))
else:
    # ret != 0（子の PID が入っている） → 自分は「親プロセス」。この print は親だけが実行する。
    print("親プロセス: pid={}, ppid={}".format(os.getpid(), os.getppid()))
