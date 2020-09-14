import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd
import time
import numpy as np

#############
#TODO
#-compare priceold to pricenew to detect changes
#-read .xlsx files
#-remove blank rows from beginning of .csv
#-if productprice = 0, or = blank, then productprice = saleprice*1.25
#############

#set directory
os.chdir('c:\\users\\mike\\Documents\\LED\\PriceSheets')

#set update mode
temp = 'z'
while temp != 's' and temp != 'p' and temp != 'b':
	temp = input("Which price are you updating?\n\
		\"p\" for productprice\n\
		\"s\" for saleprice\n\
		\"b\" for both\n\t\t".expandtabs(2))
	if temp.lower() == "s":
		newpricecol = "saleprice"
	elif temp.lower() == "p":
		newpricecol = "productprice"
	elif temp.lower() == "b":
		newpricecol = np.array(["productprice", "saleprice"])

#set markup and column names
if temp = 'b':
	markup1 = float(input("Enter markup scalar for PRODUCT price (eg 1.33 for 33% markup: "))
	markup2 = float(input("Enter markup scalar for SALE price (eg 1.25 for 25% markup: "))
	#get product code from new price sheet
	productcode_right = input("Enter name of column containing productcode on new price sheet: ").lower()
	#get columns to update
	updatecol1 = input("Enter name of the column containing new PRODUCT price: ").lower()
	updatecol = input("Enter name of the column containing new SALE price: ").lower()
else: 
	markup1 = float(input("Enter markup scalar  for (eg 1.33 for 33% markup): "))
	productcode_right = input("Enter name of column containing productcode on new price sheet: ").lower()
	updatecol1 = input("Enter name of the column containing new price: ").lower()

#get files
input("Hit enter to choose current listings file ")
Tk().withdraw()
currentprice=askopenfilename()

#while filetype == 0:
input("Hit enter to choose new price sheet ")
Tk().withdraw()
newprice=askopenfilename()

#detect delimiter of new price sheet
with open(newprice) as f:
	line = f.readline()

if len(re.split(',',line)) > 1:
	delim = ','
elif len(re.split('\t',line)) > 1:
	delim = '\t'
elif len(re.split(' ',line)) > 1:
	delim = ' '

f.close()

#read datasets
left = pd.read_csv(currentprice, encoding = "ISO-8859-1")
right = pd.read_csv(newprice, encoding = "ISO-8859-1", sep=delim, engine='python')

#make columns in 'right' dataframe lowercase so input is case insensitive
right.columns = map(str.lower, right.columns)

#remove newline from column names in 'right' dataframe
right.columns = map( lambda s: s.replace('\n',' '), right.columns)

#get column name for product code on new price sheet
productcode_right = input("Enter name of column containing productcode on new price sheet: ").lower()

#get name of column where price will be updated
updatecol = input("Enter name of the column containing new price: ").lower()

#convert right[productcode_right] to string
right[productcode_right] = right[productcode_right].astype(str)

#remove leading and trailing spaces from productcode data
right[productcode_right] = right[productcode_right].str.strip()

#remove dollar signs and commas and convert to float
if right[updatecol].dtype == np.object:
	right[updatecol] = right[updatecol].str.replace(',', '')
	right[updatecol] = right[updatecol].str.replace('$', '')
	right[updatecol] = pd.to_numeric(right[updatecol], errors='coerce')

right = right.replace(np.nan, 0, regex=True)

#replace "/" with "-" in new price sheet to match more records
right[productcode_right] = right[productcode_right].str.replace('/', '-')

#delete rows containing zero price
right = right[right[updatecol] != 0]

#narrow "right" dataframe to two necessary rows
right = right[[productcode_right, updatecol]]

################
# make some replacements in "right" dataframe to match more records
################
#get size
size = len(right.index)

#array for color temps
temps = ("27K", "3K", "35K", "4K", "5K")

def expand_temps(size1, row1, oldtext, newtext):
	right.loc[size1] = [row1[productcode_right].replace(oldtext, newtext), row1[updatecol]]

#initial replacement to correct leading digits (costless problem)
for l, row in right.iterrows():
	if re.search('^[0-9]{2}-', row[productcode_right]):
		size = size + 1
		expand_temps(size, row, row[productcode_right][:3], "")

case2 = 0
case3 = 0
case4 = 0

#search for errors in product codes and replace strings
for i, row in right.iterrows():
	#costless "(X)K" cases
	if re.search('\(X\)K', row[productcode_right]):
		case2 = 1+case2
		for j in temps:
			size = size + 1
			expand_temps(size, row, "(X)K", j)
	#costless "*K" cases
	if re.search('\*K', row[productcode_right]):
		case3 = 1+case3
		for j in temps:
			size = size + 1
			expand_temps(size, row, "*K", j)
	#costless "-K" cases
	if re.search('\-K', row[productcode_right]):
		case4 = 1+case4
		for j in temps:
			size = size + 1
			expand_temps(size, row, "-K", "-"+j)

#remove duplicates from new price sheet (right)
right = right.drop_duplicates();

#rename existing "productprice"/"saleprice" column
left.rename(inplace=True, columns={newpricecol: "oldprice"})

#use pandas to merge (left join)
joined = pd.merge(left, right, how="left", left_on="productcode", right_on=productcode_right)

#calculate marked up price
joined[updatecol] = joined[updatecol].multiply(markup)

#for i, row in joined.iterrows():
#	if re.search('T8-EZ3-2FT', row['productcode']):
#		joined.loc[i, updatecol]

#hardcoded 'case quantity' correction for westgate products
for i, row in joined.iterrows():
	if re.search('T8-EZ3-2FT|T8-EZ5', row['productcode']):
		joined.loc[i, updatecol] = row[updatecol] * 12.
	elif re.search('T8-EZ3-4FT', row['productcode']):
		joined.loc[i, updatecol] = row[updatecol] * 25.

#rename price column
joined.rename(inplace=True, columns={updatecol: newpricecol})

#create data frame for records not updated
not_updated = joined[pd.isnull(joined[newpricecol])]
#get count for unmatched records
unmatched = str(len(not_updated.index))

#delete records with no price update
updated = joined[pd.notnull(joined[newpricecol])]
#get count for matched records
matched = str(len(updated.index))

#check for price changes among matched records


#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
updated_filename = "updated_" + newpricecol + "_" + timestr + ".csv"
not_updated_filename = "not_updated_" + newpricecol + "_" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
updated_csv = updated.to_csv(path_or_buf=updated_filename, columns=["productcode",newpricecol], index=False)
not_updated_csv = not_updated.to_csv(path_or_buf=not_updated_filename, columns=["productcode",newpricecol], index=False)

#create message for user
window = Tk()
window.wm_withdraw()

#build message
if int(matched) > 0:
	countmessage = "Success!\n" + matched + " listings matched\n" + unmatched + " listings unmatched\n" + "Remember to update adder prices for matched products. This program only updates indentical SKU matches and will not change option prices" 
else:
	countmessage = "The program was unable to find any matches. Email Michael at m.hillenbrand01@gmail.com with questions"

#message at x:200,y:200
window.geometry("1x1+200+200") #remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
messagebox.showinfo(title="Program Complete",message=countmessage,parent=window)
print(countmessage)