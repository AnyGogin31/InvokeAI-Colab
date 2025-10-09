import os
import sys
import signal
import subprocess
import socket
import time


def is_port_open(port) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def signal_handler(signal, frame) -> None:
    print("\n")
    print("Ctrl+C pressed. Aborting.")
    print("Come back soon!")
    
    sys.exit(1)


def open_tunnel() -> None:
    print("Opening of the tunnel...")

    command = ["gradio-tun", "--port", "9090"]

    subprocess.Popen(command)


def bind_signal() -> None:
    signal.signal(signal.SIGINT, signal_handler)
    print("Press Ctrl+C to exit.")


def start_ngrok() -> None:
    invokeai_root_dir = os.environ["INVOKEAI_ROOT_DIR"]
    invokeai_config_path = os.environ["INVOKEAI_CONFIG_PATH"]

    command = f"invokeai-web --root {invokeai_root_dir} --config {invokeai_config_path}"
    environment = os.environ.copy()

    subprocess.Popen(
        command,
        shell = True,
        env = environment
    )

    while not is_port_open(9090):
        time.sleep(1)

    open_tunnel()
    bind_signal()

    signal.pause()


def main() -> None:
    
    if "INVOKEAI_ROOT_DIR" not in os.environ:
        raise Exception("INVOKEAI_ROOT_DIR is not set in the environment variables.")
        
    if "INVOKEAI_CONFIG_PATH" not in os.environ:
        raise Exception("INVOKEAI_CONFIG_PATH is not set in the environment variables.")

    start_ngrok()


if __name__ == '__main__':
    main()
