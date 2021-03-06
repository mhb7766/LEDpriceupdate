import csv
import pandas as pd
import numpy as np
import re

productcode_right = "ITEMNO."
updatecol = "IMAP\nPRICE"

#read csv
right = pd.read_csv("C:\\Users\\mike\\Pictures\\led\\pricesheets\\samples\\westgate_imap.csv")

#narrow "right" dataframe to two necessary rows
right = right[[productcode_right, updatecol]]

#remove newline from column names in 'right' dataframe
#right.columns = [productcode_right.replace('\n',' '), updatecol.replace('\n',' ')]

right.columns = map( lambda s: s.replace('\n',' '), right.columns)

print(right.columns)


"""
#get size
size = len(right.index)

#array for color temps
temps = ("27K", "3K", "35K", "4K", "5K")

def expand_temps(size1, row1, oldtext, newtext):
	right.loc[size1] = [row1[productcode_right].replace(oldtext, newtext), row1[updatecol]]

#initial replacement to correct leading digits
for l, row in right.iterrows():
	if re.search('^[0-9]{2}-', row[productcode_right]):
		size = size + 1
		expand_temps(size, row, row[productcode_right][:3], "")

#search for errors in product codes and replace strings
for i, row in right.iterrows():
	if re.search('\(X\)K', row[productcode_right]):
		for j in temps:
			size = size + 1
			expand_temps(size, row, "(X)K", j)
	if re.search('\*K', row[productcode_right]):
		for k in temps:
			size = size + 1
			expand_temps(size, row, "*K", k)
	#costless "-K" cases
	if re.search('\-K', row[productcode_right]):
		for k in temps:
			size = size + 1
			expand_temps(size, row, "-K", "-"+k)

print(right) """