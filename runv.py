from pytube import YouTube
import os, sys

url = input("insert link: ")
while True:
	path = os.getcwd() + "/video" 
	YouTube(url).streams.filter(file_extension="mp4", only_video=True).order_by("resolution").desc().first().download(path)
	
	url = input("insert link (or \"quit\"): ")
	if url == "quit":
		sys.exit()
