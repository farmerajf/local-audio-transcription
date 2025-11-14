#!/bin/bash

# Script to create a Python virtual environment

echo "Creating Python virtual environment..."
python3 -m venv venv

if [ $? -eq 0 ]; then
    echo "Virtual environment created successfully in ./venv"
    echo "To activate it, run: source activate_env.sh"
else
    echo "Failed to create virtual environment"
    exit 1
fi
