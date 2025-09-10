# youtube-music-dl

A YouTube music downloader written in Python using yt-dlp.

## Installation

1. Clone the repository:
	```bash
	git clone https://github.com/RetrozDev/youtube-music-dl
	cd youtube-music-dl
	```
2. Install the dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Install ffmpeg (required for audio conversion):
	- Download ffmpeg for Windows: https://www.gyan.dev/ffmpeg/builds/
	- Extract the archive and add the `bin` folder (e.g. `C:\ffmpeg\bin`) to your Windows PATH environment variable.
	- Restart your terminal after adding ffmpeg to PATH.

## Usage

Example command:
```bash
python main.py "<youtube_url>"
```

The audio will be downloaded as an mp3 file in the `downloads` folder.

## Dependencies

- yt-dlp
- ffmpeg (external, not a Python package)
