import os
import sys

from pytube import YouTube

url = input("insert link: ")
while True:
    print("downloading only_progressive...")
    path = os.getcwd() + "/mv"
    YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by("resolution").first().download(path)
    url = input("insert link (or \"quit\"): ")
    if url == "quit":
        sys.exit()
