from pytube import YouTube
import os

while True:
	url = input("insert link: ")

	yt = YouTube(url)
	path = os.getcwd() + "/music"
	yt.streams.filter(only_audio=True, file_extension='mp4').order_by("abr").first().download(path)
	print('success')

	filename = yt.title + ".mp4"
	print(filename)


