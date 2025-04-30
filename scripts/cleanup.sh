#!/bin/bash

echo "Cleaning up project directories..."

# Remove unnecessary cache files
rm -rf __pycache__

# Optimize logs
find logs/ -type f -name "*.log" -exec rm {} \;

echo "Cleanup completed!"
