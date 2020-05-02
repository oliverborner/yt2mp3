#!/usr/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg

from __future__ import unicode_literals

import youtube_dl
import sys, os


ydl_opts = {
'writethumbnail': True,
'format': 'bestaudio/best',
'outtmpl': '/Users/oliver/Music/Downloads/%(title)s.%(ext)s',  #set your output folder here
'postprocessors': [
{'key': 'FFmpegExtractAudio',
'preferredcodec': 'mp3',
'preferredquality': '192'},
{'key': 'EmbedThumbnail',},]}


#clear screen
clear = lambda: os.system('clear')
clear()

print "[ Youtube to MP3 ]"
print " "
ytlink = raw_input("insert yt-link:")
print " "
print "youtube_dl output:"

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([ytlink])

clear()
print "[ Youtube to MP3 ]"
print " "
print "- Done. File saved in Downloads folder."  #rename to your folder
print " "
