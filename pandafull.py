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
markup = float(input("Enter markup scalar (eg 1.33): "))

#get files
input("Hit enter to choose current listings file ")
Tk().withdraw()
currentprice=askopenfilename()

input("Hit enter to choose new price sheet ")
Tk().withdraw()
newprice=askopenfilename()

#read datasets
left = pd.read_csv(currentprice)
right = pd.read_csv(newprice)

#delete existing "productprice" column
left = left.drop(columns="productprice")

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on="Item No")

#get name of column where price will be updated
updatecol = input("Enter name of column containing new price ")

#calculate marked up price
joined[updatecol] = joined[updatecol].multiply(markup)

#rename price column
joined.rename(inplace=True, columns={updatecol: "productprice"})

#######
#ADD function to save new data frame with data that was not updated
#######

#create data frame for records not updated
not_updated = joined[pd.isnull(joined['productprice'])]

#delete records with no price update
updated = joined[pd.notnull(joined['productprice'])]

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
updated_filename = "updated_listings" + timestr + ".csv"
not_updated_filename = "not_updated" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
updated_csv = updated.to_csv(path_or_buf=updated_filename, columns=["productcode","productprice"], index=False)
not_updated_csv = not_updated.to_csv(path_or_buf=not_updated_filename, columns=["productcode","productprice"], index=False)
