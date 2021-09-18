from pytube import YouTube
import os

URL = input("URL: ")  # Getting URL by user.

video = YouTube(URL)  

title = video.title  # Getting video title associated to the URL from YouTube. 
print(f"\nTitle - {title}\n")  # Printing Title 

for stream in video.streams:
    print(f"Resolutions Available: {stream.resolution}")

RES = input("\nResolution: \n>>>")

video = video.streams.filter(progressive=True, res=RES).first()

PATH = input("\nPATH: \n>>>")
os.chdir(os.path.join(os.path.expanduser("~"), PATH))

video.download()
print(f"[{title}] - Downloaded Successfully!")
