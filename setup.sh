#!/bin/bash

# Setup script for local-audio-transcription project
# Run with: source setup.sh

set -e

echo "=== Local Audio Transcription Setup ==="
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

# Check if script was sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Note: Run 'source setup.sh' instead of './setup.sh' to auto-activate the environment."
    echo "Or manually activate with: source venv/bin/activate"
else
    echo "Environment is now active. Run: python transcribe.py <audio_file>"
fi

echo ""
echo "To deactivate later, run: deactivate"
