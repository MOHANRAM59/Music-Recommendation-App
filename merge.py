# import ffmpeg

# def fun(get_url):
#     input_still = input('img/music.jpeg') 
#     input_audio = input(get_url)

#     ffmpeg.output(
#         ffmpeg
#         .concat(input_still, input_audio, v=1, a=1)
#         .output("output.mp4")
#         .run(overwrite_output=True)
#     )
from moviepy.editor import ImageClip, AudioFileClip
import imageio
import numpy as np

def fun( get_url):
    audio = AudioFileClip(get_url)
    image = ImageClip('img/music.jpeg')



    duration = audio.duration

    video = image.set_duration(duration)
    video = video.set_audio(audio.set_start(0))

    video.write_videofile('output.mp4', fps=24, codec='mpeg4')
