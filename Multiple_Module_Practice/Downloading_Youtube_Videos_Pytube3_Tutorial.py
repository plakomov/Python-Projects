# Downloading youtube videos using pytube3 lib
from pytube import YouTube

url = "https://www.youtube.com/watch?v=fKl2JW_qrso"  # Need a youtube url
vid = YouTube(url) # creates a Youtube object

print(vid.title)


### NOTE: AN ERROR KEEP ON APPEARING EVERYTIME I TRY RUNNING THIS MODULE
