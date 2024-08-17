import os
import sys
import signal
import subprocess

from pyngrok import ngrok, conf


def signal_handler(signal, frame) -> None:
    print("\n")
    print("Ctrl+C pressed. Aborting.")
    print("Come back soon!")
    
    sys.exit(1)


def open_tunnel() -> None:
    print("Opening of the tunnel...")

    ngrok.kill()

    ngrok_token = os.environ["NGROK_TOKEN"]
    ngrok_domain = os.environ["NGROK_DOMAIN"]

    ngrok_config = conf.PyngrokConfig(
        auth_token = ngrok_token
    )

    server = ngrok.connect(
        9090,
        pyngrok_config = ngrok_config,
        bind_tls = True,
        domain = ngrok_domain
    ).public_url

    print(f"The tunnel is open at the link: {server}")


def bind_signal() -> None:
    signal.signal(signal.SIGINT, signal_handler)
    print("Press Ctrl+C to exit.")


def start_ngrok() -> None:
    open_tunnel()
    bind_signal()

    invokeai_root_dir = os.environ["INVOKEAI_ROOT_DIR"]
    invokeai_config_path = os.environ["INVOKEAI_CONFIG_PATH"]

    command = f"invokeai-web --root {invokeai_root_dir} --config {invokeai_config_path}"
    environment = os.environ.copy()

    subprocess.run(
        command,
        shell = True,
        env = environment
    )
    
    signal.pause()


def main() -> None:
    
    if "INVOKEAI_ROOT_DIR" not in os.environ:
        raise Exception("INVOKEAI_ROOT_DIR is not set in the environment variables.")
        
    if "INVOKEAI_CONFIG_PATH" not in os.environ:
        raise Exception("INVOKEAI_CONFIG_PATH is not set in the environment variables.")
    
    if "NGROK_TOKEN" not in os.environ:
        raise Exception("NGROK_TOKEN is not set in the environment variables.")
    
    if "NGROK_DOMAIN" not in os.environ:
        raise Exception("NGROK_DOMAIN is not set in the environment variables.")

    start_ngrok()


if __name__ == '__main__':
    main()
