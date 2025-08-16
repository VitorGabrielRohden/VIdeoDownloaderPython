import pytubefix, colorama
from pytubefix import YouTube
from colorama import Fore

while True:
    url = input(Fore.GREEN + 'Video URL: ' + Fore.RESET)
    try:
        yt = YouTube(url)
    except Exception as error:
        print(Fore.RED + 'Invalid URL')
        print(f'{error}' + Fore.RESET)
    else:
        break

print(Fore.GREEN + f'Video title: {Fore.YELLOW}{yt.title}' + Fore.RESET)
print(Fore.GREEN + 'Can download in (progressive and mp4):' + Fore.RESET)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
for i in stream:
    print(Fore.YELLOW + f'{i.resolution}, itag: {i.itag}' + Fore.RESET)

while True:
    streamin = input(Fore.GREEN + 'Itag: ' + Fore.RESET)
    try:
        stream = yt.streams.filter().get_by_itag(streamin)
        stream.download(output_path='downloadedvideos/')
    except Exception as error:
        print(Fore.RED + 'Invalid Itag')
        print(f'{error}' + Fore.RESET)
    else:
        print(Fore.GREEN + 'Video downloaded successfully' + Fore.RESET)
        break