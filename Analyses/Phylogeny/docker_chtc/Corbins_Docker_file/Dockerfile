FROM openjdk:8-jdk-slim-bullseye

RUN apt-get update && apt-get upgrade -y 
# Install stuff required later
RUN apt-get install -y curl git

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /root/

RUN if [ "$TARGETPLATFORM" = "linux/arm64" ]; then  curl -fsSLO https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.aarch64.tgz; else  curl -fsSLO https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.aarch64.tgz; fi

RUN tar -xzf BEAST*.tgz

# Add BEAST 2
# RUN curl -fsSLO https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.aarch64.tgz \
# 	&& tar fxz BEAST.v2.7.7.Linux.aarch64.tgz 
ENV PATH="/root/beast/bin:$PATH"

# Install BEAGLE
RUN apt-get update && apt-get install -y cmake build-essential autoconf automake libtool pkg-config
RUN git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git 

RUN cd beagle-lib \
    && mkdir build \
    && cd build \
    && if [ "$TARGETPLATFORM" = "linux/arm64" ]; then  cmake -DBUILD_SSE=OFF -DBUILD=_CUDA=OFF ..; else  cmake ..; fi \ 
    && make install \
    && ldconfig

ENV LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"

RUN chown -hR root /root/beast
RUN chmod -R 777 /root/ && chmod -R 777 /usr/local/lib && chmod -R 777 /root/beast

# Add BEAST 2 packages:
RUN packagemanager -add ORC
RUN packagemanager -add BICEPS
RUN packagemanager -add starbeast3

ENV PATH="/root/beast/bin:$PATH"