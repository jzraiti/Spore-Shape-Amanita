#!/bin/bash

# Run BEAST with 4 threads and the specified XML file

# Install required BEAST packages
packagemanager -add ORC
packagemanager -add BICEPS
packagemanager -add starbeast3

beast -beagle_instances 6 -threads 24 yourfile.xml
