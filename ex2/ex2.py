import subprocess


def generate_mosaic(vid1, vid2, vid3, vid4, out):
    command = f"""ffmpeg -i {vid1} -i {vid2} -i {vid3} -i {vid4} -filter_complex "nullsrc=size=640x480 [base]; [0:v] 
    setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] 
    setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][
    upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] 
    overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" -c:v libx264 {out} """

    subprocess.call(command, shell=True)


generate_mosaic('160x120_vp8.webm', '160x120_vp9.webm', '160x120_h265.mp4', '160x120_av1.mkv', '160x120_mosaic.mkv')
generate_mosaic('360x240_vp8.webm', '360x240_vp9.webm', '360x240_h265.mp4', '360x240_av1.mkv', '360x240_mosaic.mkv')
generate_mosaic('480p_vp8.webm', '480p_vp9.webm', '480p_h265.mp4', '480p_av1.mkv', '480p_mosaic.mkv')
generate_mosaic('720p_vp8.webm', '720p_vp9.webm', '720p_h265.mp4', '720p_av1.mkv', '720p_mosaic.mkv')