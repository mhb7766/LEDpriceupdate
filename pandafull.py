import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
#from pathlib import path
import time

#############
#TODO
#-check for zero prices
#-set decimal places to 2
#
#############

#set directory
os.chdir('c:\\users\\mike\\pictures\\led')

#set markup
markup = input("Enter markup scalar: ")

#get files
input("Hit enter to choose current listings file")
Tk().withdraw()
currentprice=askopenfilename()

input("Hit enter to choose new price sheet ")
Tk().withdraw()
newprice=askopenfilename()

#read datasets
left = pd.read_csv(currentprice)
right = pd.read_csv(newprice)

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on="Item No")

#get name of column where price will be updated
updatecol = input("Enter column name containing new price")

#calculate price
joined[updatecol] = joined[updatecol].multiply(markup)

#rename price column
joined.rename(inplace=True, columns={updatecol: "productprice"})

#######
#ADD function to save new data frame with data that was not updated
#######

#delete records with no price update
joined = joined[pd.notnull(joined['productprice'])]

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
filename = "readyforupoad" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
newsheet = joined.to_csv(path_or_buf=filename, columns=["productcode","productprice"], index=False)