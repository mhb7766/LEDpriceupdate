import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd
#from pathlib import path
import time

#############
#TODO
#-compare priceold to pricenew to detect changes
#-finish README
#############

#set directory
os.chdir('c:\\users\\mike\\pictures\\led')

#set update mode
flag = 0
while flag == 0:
	temp = input("Which price are you updating? Enter \"P\" for productprice and \"S\" for saleprice: ")
	if temp.lower() == "s":
		newpricecol = "saleprice"
		flag = 1
	elif temp.lower() == "p":
		newpricecol = "productprice"
		flag = 1

#set markup
markup = float(input("Enter markup scalar (eg 1.33): "))

#get files
input("Hit enter to choose current listings file ")
Tk().withdraw()
currentprice=askopenfilename()

input("Hit enter to choose new price sheet ")
Tk().withdraw()
newprice=askopenfilename()

#get column name for product code on new price sheet
productcode_right = input("Enter name of column containing productcode on new price sheet: ")

#get name of column where price will be updated
updatecol = input("Enter name of the column containing new price ")

#read datasets
left = pd.read_csv(currentprice)
right = pd.read_csv(newprice)

#delete rows containing zero pric
right = right[right[updatecol] != 0]

#rename existing "productprice"/"saleprice" column
left.rename(inplace=True, columns={newpricecol: "oldprice"})

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on=productcode_right)

#calculate marked up price
joined[updatecol] = joined[updatecol].multiply(markup)

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
matched = 

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
updated_filename = "updated_listings" + timestr + ".csv"
not_updated_filename = "not_updated" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
updated_csv = updated.to_csv(path_or_buf=updated_filename, columns=["productcode",newpricecol], index=False)
not_updated_csv = not_updated.to_csv(path_or_buf=not_updated_filename, columns=["productcode",newpricecol], index=False)

#create message for user
window = Tk()
window.wm_withdraw()

#build message
countmessage = "Success!\n" + matched + " listings matched\n" + unmatched + " listings unmatched\n" + "Remember to update adder prices for matched products. This program only updates indentical SKU matches and will not change options" 

#message at x:200,y:200
window.geometry("1x1+200+200") #remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
messagebox.showinfo(title="Program Complete",message=countmessage,parent=window)
print(countmessage)