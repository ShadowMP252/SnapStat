FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    wget \
    libboost-all-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    && curl -Lo lazygit.tar.gz https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_0.54.2_linux_x86_64.tar.gz \
    && tar xf lazygit.tar.gz lazygit \
    && install lazygit /usr/local/bin \
    && rm -rf lazygit lazygit.tar.gz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
RUN python3 -m venv /workspace/.venv
ENV PATH="/workspace/.venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel


CMD ["bash"]