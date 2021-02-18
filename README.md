# AutoWaller

Autowaller is a python script written for cahning linux desktop background for every phase of the daty from morning to evening.

The script is written is python and uses datetime and os module for finding time and executing the command "gsettings" to change the wallpaper. 

Sample linux command for gsettings 

```
gsettings set org.gnome.desktop.background picture-uri file:///home/gautamsood/Pictures/Wallpapers/early_night.jpg
```
To run the script we need to edit crontab using below command
``` 
crontab -e
```

