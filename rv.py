import os
import sys

from pytube import YouTube

url = input("insert link: ")
while True:
    path = os.getcwd() + "/video"
    YouTube(url).streams.filter(file_extension="mp4").order_by("resolution").desc().first().download(path)

    path = os.getcwd() + "/video_m"
    YouTube(url).streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first().download(
        path)

    url = input("insert link (or \"quit\"): ")
    if url == "quit":
        sys.exit()
