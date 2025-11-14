#!/bin/bash

# Script to activate the Python virtual environment

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Run ./create_env.sh first."
    exit 1
fi

echo "To activate the virtual environment, run:"
echo "source venv/bin/activate"
