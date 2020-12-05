import subprocess


def streaming(video, host, port):
    command = f"ffmpeg -re -i {video} -f mpgets udp://{host}:{port}"
    subprocess.call(command, shell=True)

