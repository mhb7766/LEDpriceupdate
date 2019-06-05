import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
#from pathlib import path
import time

#set directory
os.chdir('c:\\users\\mike\\pictures\\led')

#get files
input("Hit enter to choose current listings file: ")
Tk().withdraw()
currentprice=askopenfilename()

input("Hit enter to choose new price sheet: ")
Tk().withdraw()
newprice=askopenfilename()

#get name of columns where price will be updated?
saleprice_col = input("Enter column name containing new list price: ")
hotprice_col = input("Enter column name containing new hot price: ")

#get name of column with productcode from price sheet
productcode_col = input("Enter column name containg productcode on price sheet")

#read datasets
left = pd.read_csv(currentprice)
right = pd.read_csv(newprice)

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on=productcode_col)

#rename price column
joined.rename(inplace=True, columns={saleprice_col: "productpricenew"})
joined.rename(inplace=True, columns={hotprice_col: "hotpricenew"})

#delete records with no price update
joined = joined[pd.notnull(joined['productpricenew'])]

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
filename = "readyforupoad" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
newsheet = joined.to_csv(path_or_buf=filename, columns=["productcode","productprice","saleprice","productpricenew","hotpricenew"], index=False)