from pathlib import Path
import os
import re
from sys import argv

dwl = "C:\\Testing\\Downloads" #Downloads folder
wtc = "C:\\Testing\\Watched" #Watched folder
file = argv[1]

end = 'AVI|MKV|MP4|M4V|FLV|WMV|MPG' #File endings
video = re.match(r'(.*)\.(' + end + ')$', file) #Check if the file is a video

if video:
	name = video.group(1).replace('.', ' ').strip() #Remove dots between words

	#Match TV shows with name format S00E00
	tv = re.match(r'(.*)([S|s][0-9]{1,2}[E|e][0-9]{1,2})(.*)', name)

	#Strip away unnecessary title information
	#Create a folder with the TV show name
	wtc = wtc + "\\" + tv.group(1).strip()
	if not os.path.exists(wtc):
		os.mkdir(wtc)

	#Make sure this also happens if the file does not exist
	name = tv.group(1) + tv.group(2).strip() + '.' + video.group(2).strip()

	if tv:
		#Create folder for TV show if it doesn't exist
		if not os.path.exists(wtc + "\\" + tv.group(1).strip()):
			os.rename(dwl + "\\" + file, wtc + "\\" + name) #Move file
	os.startfile(wtc + "\\" + name) #Open file
else:
	print("file not found")