FROM python:3.7-stretch

COPY docker/requirements.system /root/requirements.system
COPY docker/docker_requirements.txt /root/docker_requirements.txt
COPY requirements.txt /root/requirements.txt
COPY docker/configure_extra_settings.sh configure_extra_settings.sh
COPY AltaLab /root/AltaLab

RUN apt-get update \
    && xargs apt-get install -y  < /root/requirements.system \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /root/requirements.system

RUN pip install --upgrade pip==19.3.1
RUN pip install -e /root/AltaLab
RUN pip install -r /root/docker_requirements.txt
RUN pip install -r /root/requirements.txt
RUN bash configure_extra_settings.sh

ENTRYPOINT [ "bash" ]
