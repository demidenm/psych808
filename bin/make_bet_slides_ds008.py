#!/usr/bin/env python

#htmldir = '/nfs/turbo/arcts-dads-nii-open/demidenm/ds008/sub001/anatomy/bet_slices.html'
subj = 1

#open file bin_slices.htmlt
dirfileopen = open('/home/demidenm/Projects/ds008/sub001/anatomy/bet_slices.html')

for text in dirfileopen:
#print the files  contents into praces
	text.find('{:03d}')
	print(text.format(subj))
	text.write()

