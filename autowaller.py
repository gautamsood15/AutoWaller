#!/usr/bin/python

import os 
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
hr,mn,sec = str(current_time).split(":")

hr = int(hr)

if 5 > hr >= 0:
	print("Late Night")
elif 8 > hr >= 5:
	print("Early Morning")
elif 12 > hr >= 8:
	print("Late Morning")
elif 18 >= hr >= 12:
	print("Afternoon")
elif 23 >= hr > 18:
	print("Early Night")
else:
	print("Invalid Hour")



#os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/firewatch_afternoon.jpg')

