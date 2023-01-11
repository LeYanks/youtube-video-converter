import os 
from pathlib import Path
from pytube import Playlist

link = Playlist(str(input("Entrez l'URL de la playlist YouTube : ")))

path = os.path.expanduser("~/Downloads/"+link.title) 

os.mkdir(path)

for video in link.videos:
    video.streams.get_highest_resolution().download(path)
    print("Video téléchargée: ", video.title)

print("La playlist: " +link.title+ " a été téléchargée.")
