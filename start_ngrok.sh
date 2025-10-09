#!/bin/bash

echo "Activation of the environment..."
eval "$(conda shell.bash hook)"
conda activate "$INVOKEAI_KERNEL_NAME"

echo "Launch InvokeAI (Ngrok)..."
pip install pyngrok
python start_ngrok.py

echo "InvokeAI is complete..."
