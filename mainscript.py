from pytube import YouTube
import path
import exceptions
import os
import res_fps
print("Paste Last video URL in playlist here:")
MAIN_URL = input()
name=MAIN_URL.split("=")
n=int(name[-1])
try:
    yt = YouTube(MAIN_URL)
except:
    exceptions.check(MAIN_URL)
resval = res_fps.res(yt)
temp=yt
for i in range (1,n+1):
    URL=MAIN_URL.replace(name[-1], str(i))
    try:
        yt = YouTube(URL)
    except:
        exceptions.check(URL)
    video = yt.streams.filter(file_extension="mp4",resolution=resval).first()
    path = path.mkdir(yt)
    if(path=="already exits"):
        exit()
    if(video.download(path)):
        print("\nDownload success!!!\n")
    else:
        print("An unfortunate error has occured...\n")

