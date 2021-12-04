from pytube import YouTube
import argparse, sys, os


def main(args):
    parser = argparse.ArgumentParser(description="Parsing Argument")
    parser.add_argument("--url", type=str, required=False)
    args = parser.parse_args(args)
    yt_url = ""
    if args.url is not None:
        yt_url = args.url
    else:
        yt_url = input("Insert URL: ")
    print("yt url is..." + yt_url)
    while True:
        yt = YouTube(yt_url)
        path_m = os.getcwd() + "/music"
        path_v = os.getcwd() + "/video"
        path_mv = os.getcwd() + "/mv"
        path_adaptive = os.getcwd() + "/adaptive"

        filename = yt.title + ".mp4"
        stream = yt.streams
        print("downloading only_audio...")
        stream.filter(only_audio=True, file_extension='mp4').order_by("abr").desc().first().download(path_m)
        print("downloading only_video...")
        stream.filter(only_video=True, file_extension='mp4').order_by("resolution").desc().first().download(path_v)
        print("downloading progressive...")
        stream.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download(path_mv)
        print("downloading adaptive...")
        stream.filter(adaptive=True, file_extension='mp4').order_by("resolution").desc().first().download(path_adaptive)
        print('success')

        yt_url = input("Insert URL or type \"quit\": ")
        if yt_url == "quit":
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
