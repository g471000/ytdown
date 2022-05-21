from pytube import YouTube
import os, sys

url = input("insert link: ")
while True:
	path = os.getcwd() + "/video"

	stream = YouTube(url).streams
	print(stream.filter(file_extension="mp4", only_video=True).order_by("resolution").desc())

	itag = input('Type itag: ')
	stream.get_by_itag(itag).download(path)

	url = input("insert link (or \"quit\"): ")
	if url == "quit":
		sys.exit()
