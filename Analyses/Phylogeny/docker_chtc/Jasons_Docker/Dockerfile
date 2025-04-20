FROM openjdk:8-jdk-slim-bullseye

# Set non-interactive mode for apt
ARG DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        cmake \
        build-essential \
        autoconf \
        automake \
        libtool \
        pkg-config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /root/

# Download and extract BEAST 2 based on architecture
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        curl -fsSL https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.x86.tgz -o BEAST.tgz; \
    elif [ "$ARCH" = "aarch64" ]; then \
        curl -fsSL https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.aarch64.tgz -o BEAST.tgz; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    tar -xzf BEAST.tgz && \
    rm BEAST.tgz

# Add BEAST 2 to PATH
ENV BEAST_HOME="/root/beast"
ENV PATH="$BEAST_HOME/bin:$PATH"

# Clone and build BEAGLE library
RUN git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git && \
    cd beagle-lib && \
    mkdir build && \
    cd build && \
    cmake -DBUILD_SSE=OFF -DBUILD_CUDA=OFF .. && \
    make install && \
    ldconfig && \
    cd /root && rm -rf beagle-lib

# Set library path
ENV LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"

# Create a non-root user
RUN useradd -m -s /bin/bash containeruser && \
    mkdir -p /home/containeruser/beast /scratch && \
    cp -r /root/beast/* /home/containeruser/beast/ && \
    chown -R containeruser:containeruser /home/containeruser/beast /usr/local/lib /scratch

# Switch to non-root user
USER containeruser

# Ensure PATH is updated for the non-root user
ENV BEAST_HOME="/home/containeruser/beast"
ENV PATH="$BEAST_HOME/bin:$PATH"

# Install required BEAST packages
RUN packagemanager -add ORC
RUN packagemanager -add BICEPS
RUN packagemanager -add starbeast3

# Set working directory for the user
WORKDIR /scratch

# Copy all .xml .sh files from the build context into the container
COPY *.xml /scratch/
COPY *.sh /scratch/