# Import Youtube library first
# if you didn't have pytube or getting runtime error
# Then you have to download the pytube library using CMD
# Type : pip install pytube

from pytube import youtube

# here is the URL of youtube video
url = "https://www.youtube.com/watch?v=ZXgOXuhXtuI"
yt = p.YouTube(url)
video = yt.streams.first()

# here is the path of download video
video.download("C://Users//Seraj//Downloads")
