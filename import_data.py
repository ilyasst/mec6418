# -*- coding: utf-8 -*-
import csv
import os

def import_data_04_01( file_name ):
	i = 0
	time = []
	deformation = []
	
	with open( file_name, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if i == 0:
				i = i + 1
				pass
			else:
				i = i + 1
				time.append(float(row[0]))
				deformation.append( float(row[1]) )

	return time, deformation