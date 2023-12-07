FROM archlinux:latest
USER root
RUN pacman-key --init
RUN pacman -Syu --noconfirm python wget tar python-requests msr-tools
COPY main.py requirements.txt /xmrig-py/
WORKDIR /xmrig-py
RUN python main.py
WORKDIR /xmrig-py/xmrig
CMD ./xmrig -k -a rx/0 -o $pool -u $wallet -p $worker_name
