from pytube import YouTube

# https://www.youtube.com/watch?v=LXb3EKWsInQ
# https://youtu.be/fVr_yM5Q1vs

url = input("input url here: ")
yt = YouTube(url)

for stream in yt.streams.filter(file_extension="mp4", adaptive=True, progressive=False, res="1080p"):
    print(stream)


# for stream in yt.streams.filter(only_audio=True, file_extension="mp4"):
#     print(stream)
