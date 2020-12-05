# SCAV-SEMI3

## Mar Vidal-Folch Angerri - NIA: 204751

In this seminar we have worked with ffmpeg and streaming.

### Exercise 1
---
In this exercise we have created a python script able to convert videos into the following codecs:
- vp8
- vp9
- h.265
- av1 \\
Getting the videos from previous labs, we converted the 10 seconds BBB videos in different bitrates to the different codecs. The qualities used were the following ones:  
- 720p (which corresponds to 1280x720 pixels)
- 480p (whose standard corresponds to 640x480 pixels) 
- 360x240
- 160x120 \\
So, the script outputs 16 different videos. You can find the script and the outputs in ex1 folder. 

### Exercise 2
---
In this exercise we have created a python script to generate 4 video mosaics. In each of them, we find the videos with the same bitrate but in different codecs. The videos are displayed following this order: 
- Upper-left: vp8 codec
- Upper-right: vp9 codec
- Lower-left: h.265 codec
- Lower-right: av1 codec \\
After analyzing the results:
- The truth is that by looking at the output videos I couldn't find lots of differences between them. However:
- vp9 is better than vp8: we see that the video quality is better when using vp9 codec than when using vp8 codec. This fact makes sense as the vp9 is the improved version of vp8 and, theoretically, the encoder is better. \\
You can find the script used to generate the mosaics and the output files in ex2 folder. 
### Exercises 3-4
---
The goal of these two exercises is to create a live streaming using ffmpeg. We hace created a pyhton script in order to do it, which you can find in ex3-4 folder. 
