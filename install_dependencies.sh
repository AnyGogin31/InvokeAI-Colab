#!/bin/bash

echo "Creating an environment..."
conda create -p $INVOKEAI_KERNEL_PREFIX python=3.10 -y

echo "Activation of the environment..."
eval "$(conda shell.bash hook)"
conda activate "$INVOKEAI_KERNEL_NAME"

echo "Installing dependencies InvokeAI..."
pip install InvokeAI --use-pep517 --extra-index-url https://download.pytorch.org/whl/cu121
pip install "InvokeAI[xformers]" --use-pep517

echo "Installing additional packages..."
conda install -c conda-forge gcc=12.1.0 -y
pip install pyngrok
pip install matplotlib-inline

echo "Disconnecting from the environment..."
conda deactivate

echo "Installation complete."
