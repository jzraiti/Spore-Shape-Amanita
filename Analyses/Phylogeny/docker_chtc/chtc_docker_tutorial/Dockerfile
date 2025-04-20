# Build the image based on the official Python version 3.8 image
FROM python:3.8

# Our base image happens to be Debian-based, so it uses apt-get as its system package manager
# Use apt-get to install wget 
RUN apt-get update \
 && apt-get install wget

# Use RUN to install Python packages (numpy and scipy) via pip, Python's package manager
RUN pip3 install numpy scipy

