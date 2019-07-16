import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
#from pathlib import path
import time
import numpy as np

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
#updatecol = input("Enter column name containing new price: ")

#get name of column with productcode from price sheet
productcode_right = input("Enter column name containing productcode on price sheet: ")

#read datasets
left = pd.read_csv(currentprice)
right = pd.read_csv(newprice)

#remove dollar signs and commas and convert to float
#if right[updatecol].dtype == np.object:
#	right[updatecol] = right[updatecol].str.replace(',', '')
#	right[updatecol] = right[updatecol].str.replace('$', '')
#	right[updatecol] = pd.to_numeric(right[updatecol], errors='coerce')

right = right.replace(np.nan, 0, regex=True)

#replace "/" with "-" in new price sheet to match more records
right[productcode_right] = right[productcode_right].str.replace('/', '-')

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on=productcode_right)

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
filename = "merged" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
newsheet = joined.to_csv(path_or_buf=filename, index=False)