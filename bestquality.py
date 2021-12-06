from pytube import YouTube
import ffmpeg

# https://www.youtube.com/watch?v=LXb3EKWsInQ
# https://youtu.be/fVr_yM5Q1vs

url = input("input url here: ")
yt = YouTube(url)

stream = yt.streams.filter(adaptive=True, progressive=False).first()
stream.download('temp', filename="video.mp4")

audio = yt.streams.filter(adaptive=True, progressive=False, only_audio=True).first()
audio.download('temp', filename="audio.mp4")

video_stream = ffmpeg.input('temp/video.mp4')
audio_stream = ffmpeg.input('temp/audio.mp4')
ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()
