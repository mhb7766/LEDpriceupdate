import csv
import pandas as pd
import numpy as np
import re

productcode_right = "Item No"
updatecol = "Price A"

#read csv
right = pd.read_csv("newpriceshort.csv")

#narrow "right" dataframe to two necessary rows
right = right[[productcode_right, updatecol]]

#get size
size = len(right.index)

for i, row in right.iterrows():
	if re.search('\(X\)K', row[productcode_right]):
		size = size + 1
		right.loc[size] = [row[productcode_right].replace("(X)K", "27K"), row[updatecol]]
		size = size + 1
		right.loc[size] = [row[productcode_right].replace("(X)K", "3K"), row[updatecol]]
		size = size + 1
		right.loc[size] = [row[productcode_right].replace("(X)K", "35K"), row[updatecol]]
		size = size + 1
		right.loc[size] = [row[productcode_right].replace("(X)K", "4K"), row[updatecol]]
		size = size + 1
		right.loc[size] = [row[productcode_right].replace("(X)K", "5K"), row[updatecol]]

print(right)

#with open("onsite_6-18.csv", "r") as rfh, open("newpriceshort.csv", "a") as wfh:
#	r = csv.reader(rfh, delimiter=',')
#	w = csv.writer(wfh)
#	w.writerow("********TEST************, *****************MAXLITE TEST, 100, 100, 100, ")
#	for row in r:
		