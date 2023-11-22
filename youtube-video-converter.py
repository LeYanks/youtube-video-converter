from pathlib import Path
from pytube import YouTube

# Demander à l'utilisateur l'URL de la vidéo YouTube
url = input("Entrez l'URL de la vidéo YouTube : ")
yt = YouTube(url)

# Demander à l'utilisateur le dossier de destination pour le téléchargement
destination_folder = input("Entrez le chemin complet du dossier de destination : ")
download_path = Path(destination_folder)

# Vérifier si le dossier de destination existe, sinon le créer
if not download_path.exists():
    download_path.mkdir(parents=True, exist_ok=True)

# Télécharger la vidéo avec la meilleure résolution disponible dans le dossier spécifié
video = yt.streams.get_highest_resolution()
video.download(download_path)

# Afficher un message une fois la vidéo téléchargée
print(f'La vidéo "{yt.title}" a été téléchargée dans {download_path}.')
