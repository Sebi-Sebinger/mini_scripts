#!/bin/bash
echo test
mode=$(gsettings get org.gnome.desktop.interface color-scheme)
echo $mode
if [[ $mode == "'prefer-dark'" ]]; then
	echo 'in dark'
	gsettings set org.gnome.desktop.background picture-uri file://$HOME/Bilder/Hintergründe/dark.jpeg
else
	echo 'in light'
	gsettings set org.gnome.desktop.background picture-uri file://$HOME/Bilder/Hintergründe/light.jpg
fi

