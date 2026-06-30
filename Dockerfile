FROM ubuntu:20.04

# tzdata などの対話プロンプトを抑止（コンテナ実行時には残さない）
ARG DEBIAN_FRONTEND=noninteractive

# 本(linux-in-practice-2nd)の README に記載のパッケージ一式
RUN apt-get update && apt-get install -y \
        binutils build-essential golang sysstat \
        python3-matplotlib python3-pil fonts-takao fio \
        qemu-kvm virt-manager libvirt-clients virtinst jq \
        docker.io containerd libvirt-daemon-system strace \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY hello.go hello.py inf-loop.py syscall-inf-loop.py fork.py intignore.py ./
RUN chmod +x hello.py inf-loop.py syscall-inf-loop.py fork.py intignore.py \
    && go build -o hello hello.go

CMD ["/bin/bash"]
