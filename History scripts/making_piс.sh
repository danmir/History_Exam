#!/bin/bash
# Making pictures from text files
# Put in working dir (doesn't work with paths that contain spaces)
for f in `gfind "$PWD" -maxdepth 2  -name "*.txt" | sort -n -t _ -k 3`; do
	echo "$f"
	convert -size 480x480 xc:white -pointsize 14 -gravity center -fill black label:@$f "$f".png
done

for f in `gfind "$PWD" -maxdepth 2  -name "*-0.png"`; do
	echo "$f"
	grm "$f"
done
