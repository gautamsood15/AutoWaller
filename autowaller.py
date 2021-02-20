#!/usr/bin/python

import os 
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
hr,mn,sec = str(current_time).split(":")

hr = int(hr)







#os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/firewatch_afternoon.jpg')

