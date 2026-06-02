# linux-practice

「Linuxのしくみ 増補改訂版」（[linux-in-practice-2nd](https://github.com/satoru-takeuchi/linux-in-practice-2nd)）の
実験を動かすための Docker 環境。本が前提とする Ubuntu 20.04 / x86_64 に合わせている。

## 使い方

```sh
# ビルド（arm64 ホストでは --platform を付ける）
docker build --platform linux/amd64 -t linux-practice .

# 起動
docker run --platform linux/amd64 -it --rm linux-practice
```

x86_64 の Linux ホストなら `--platform linux/amd64` は不要。

## サンプルコードの実行

コンテナ起動後、`/work` に移動済みなのでそのまま実行できる。

```sh
./hello          # Go
python3 hello.py # Python
```

## 注意

`qemu-kvm` / `libvirt` は入れてあるが、VM の起動にはホストの `/dev/kvm` が必要で、
Docker Desktop for Mac では使えない。それ以外の実験（計測・作図・ビルド系）は動く。
