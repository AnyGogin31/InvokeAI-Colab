#!/bin/bash

echo "Activation of the environment..."
eval "$(conda shell.bash hook)"
conda activate "$INVOKEAI_KERNEL_NAME"

echo "Launch InvokeAI (Gradio)..."
pip install gradio-tunneling
python start_gradio.py

echo "InvokeAI is complete..."
