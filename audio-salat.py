#%%


import optparse
import ffmpeg
import numpy as np


f1='./video/GitS-SAC-S01E01-Section_9-ger.mp4'
f2='./video/GitS-SAC-S01E01-Section_9-eng.mkv'
f3=str('C:\Users\simon\Downloads\workspace\SPYDER\AudioSalat\video\GitS-SAC-S01E01-Section_9-ger.mp4')

probe = ffmpeg.probe(f3)
print(probe)



