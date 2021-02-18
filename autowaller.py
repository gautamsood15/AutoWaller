#!/usr/bin/env python3

import os 
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
hr,mn,sec = str(current_time).split(":")

hr = int(hr)

os.system("touch test.txt")

if 5 > hr >= 0:
	os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/late_night.jpg')
elif 8 > hr >= 5:
	os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/early_morning.jpg')
elif 12 > hr >= 8:
	os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/late_morning.jpg')
elif 18 >= hr >= 12:
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/afternoon.jpg")
elif 23 >= hr > 18:
	os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/early_night.jpg')
else:
	print("Invalid Hour")


