# importing the module
import argparse
from pytube import YouTube

# folder to save video
SAVE_PATH = "vid/"

extract = argparse.ArgumentParser()
extract.add_argument(
    "link", help="Link of video which you want to download(provide in string format)", type=str)
# link of the video to be downloaded
args = extract.parse_args()

ln = args.link
yt = YouTube(ln)

resobj = yt.streams
try:
    # download the video
    resobj[11].download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')
