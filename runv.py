from pytube import YouTube
import os

while True:
	url = input("insert link: ")
	path = os.getcwd() + "/video" 
	YouTube(url).streams.filter(file_extension="mp4", only_video=True).order_by("resolution").desc().first().download(path)
