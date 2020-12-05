import subprocess


def convert_vp8_vp9_h265_av1(video, out_vp8, out_vp9, out_h265, out_av1):
    # convert to vp8:
    command = f"ffmpeg -i {video} -c:v libvpx -b:v 1M -c:a libvorbis {out_vp8}"  # .webm
    subprocess.call(command, shell=True)

    # convert to vp9:
    command = f"ffmpeg -i {video} -c:v libvpx-vp9 -b:v 2M {out_vp9}"  # .webm
    subprocess.call(command, shell=True)

    # convert to h.265:
    command = f"ffmpeg -i {video} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k {out_h265}"  # .mp4
    subprocess.call(command, shell=True)

    # convert to av1
    command = f"ffmpeg -i {video} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental {out_av1}"  # .mkv
    subprocess.call(command, shell=True)


convert_vp8_vp9_h265_av1('160x120.mp4', '160x120_vp8.webm', '160x120_vp9.webm', '160x120_h265.mp4', '160x120_av1.mkv')
convert_vp8_vp9_h265_av1('360x240.mp4', '360x240_vp8.webm', '360x240_vp9.webm', '360x240_h265.mp4', '360x240_av1.mkv')
convert_vp8_vp9_h265_av1('480p.mp4', '480p_vp8.webm', '480p_vp9.webm', '480p_h265.mp4', '480p_av1.mkv')
convert_vp8_vp9_h265_av1('720p.mp4', '720p_vp8.webm', '720p_vp9.webm', '720p_h265.mp4', '720p_av1.mkv')