from pathlib import Path
from pytube import YouTube

link = YouTube(str(input("Entrez l'URL de la vidéo YouTube : ")))

path = link.streams.get_highest_resolution().download(Path.home() / "Downloads") 

print(link.title + " a été téléchargée.")
