#!/bin/bash

# Install required BEAST packages
packagemanager -add ORC
packagemanager -add BICEPS
packagemanager -add starbeast3

# Run BEAST with 4 threads and the specified XML file
beast -threads 4 beast.xml