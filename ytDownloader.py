from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(r'C:\Users\bashi\OneDrive\Documents\DownloadedVideos') #Make sure to change this line to the directory where you would like to save the video
