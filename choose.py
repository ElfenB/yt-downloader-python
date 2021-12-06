from pytube import YouTube
import ffmpeg

# https://www.youtube.com/watch?v=LXb3EKWsInQ
# https://youtu.be/fVr_yM5Q1vs

url = input("input url here: ")
yt = YouTube(url)

for stream in yt.streams.filter():
    print(stream)

video_stream_id = int(input("video stream id: "))
audio_stream_id = int(input("audio stream id: "))

stream = yt.streams.get_by_itag(video_stream_id)
stream.download('temp', filename="video.mp4")

audio = yt.streams.get_by_itag(audio_stream_id)
audio.download('temp', filename="audio.mp4")

video_stream = ffmpeg.input('temp/video.mp4')
audio_stream = ffmpeg.input('temp/audio.mp4')
ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()
