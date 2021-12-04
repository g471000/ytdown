from pytube import YouTube
import argparse, sys, os

def main(args):
	parser = argparse.ArgumentParser(description="Parsing Argument")
	parser.add_argument("--url", type=str, required=False)
	args = parser.parse_args(args)
	yt_url = ""
	if args.url != None:
		yt_url = args.url	
	else:
		yt_url = input("Insert URL: ")	
	print("yt url is..." + yt_url)
	while True:
		yt = YouTube(yt_url)
		path_m = os.getcwd() + "/music"
		path_v = os.getcwd() + "/video"

		filename = yt.title + ".mp4"
		yt.streams.filter(only_audio=True, file_extension='mp4').order_by("abr").first().download(path_m)
		yt.streams.filter(only_video=True, file_extension='mp4').order_by("resolution").first().download(path_v)
		print('success')


		yt_url = input("Insert URL or type \"quit\": ")
		if yt_url == "quit":
			sys.exit()


if __name__ == '__main__':
	main(sys.argv[1:])
