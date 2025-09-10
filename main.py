import sys
import os
import yt_dlp

AUDIO_DL_DIR = './downloads'

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(AUDIO_DL_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print('Download finished!')
        except Exception as e:
            print(f'Failed to download: {e}')

if __name__ == "__main__":
    if not os.path.exists(AUDIO_DL_DIR):
        os.makedirs(AUDIO_DL_DIR)
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_url>")
        sys.exit(1)
    url = sys.argv[1]
    download_audio(url)