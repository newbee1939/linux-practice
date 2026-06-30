#!/usr/bin/python3

import signal

# Ctrl + C（SIGINT）が届いたときの挙動をカスタマイズ
# SIGINTシグナルを無視するように設定。
# 第一引数にはハンドラを設定するシグナルの番号を指定（ここではsignal.SIGINT）
# 第二引数にはシグナルハンドラ関数を指定（ここではsignal.IGN）
signal.signal(signal.SIGINT, signal.SIG_IGN)

# 無限ループ
while True:
    pass
