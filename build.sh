#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt
pip install pyinstaller

echo "Building executable..."
pyinstaller DesktopPet.spec

echo "Build complete! Executable is in dist/DesktopPet"
