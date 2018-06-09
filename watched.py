from pathlib import Path
import os
from sys import argv

dwl = "C:\\Testing\\Downloads" #Downloads folder
wtc = "C:\\Testing\\Watched" #Watched folder
file = argv[1]

os.rename(dwl + "\\" +file, wtc + "\\" +file) #Move file
os.startfile(wtc + "\\" +file) #Open file