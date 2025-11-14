#!/bin/bash

# Initial setup script for open-whisper-transcribe project

set -e

echo "=== Open Whisper Transcribe Setup ==="
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Step 1: Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Step 1: Virtual environment already exists."
fi

echo ""
echo "Step 2: Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Step 3: Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Step 4: Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To use the transcription tool:"
echo "  1. Activate the environment: source venv/bin/activate"
echo "  2. Run transcription: python transcribe.py <audio_file.m4a>"
echo ""
echo "To deactivate the environment later, run: deactivate"
