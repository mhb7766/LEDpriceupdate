import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
#from pathlib import path
import time

#set directory
os.chdir('c:\\users\\mike\\pictures\\led')

#maybe get name of column where price will be updated?



#set markup
markup = 1.33

#read datasets
left = pd.read_csv('example.csv')
right = pd.read_csv('allmax_ex.csv')

#use pandas to merge
joined = pd.merge(left, right, how="left", left_on="productcode", right_on="Item#")

#calculate price
joined['A Price'] = joined['A Price'].multiply(markup)

#rename price column
joined.rename(inplace=True, columns={"A Price": "productprice"})

#delete records with no price update
joined = joined[pd.notnull(joined['productprice'])]

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
filename = "readyforupoad" + timestr + ".csv"

#convert pandas datafram to .csv and save (keeps only 'productcode and product price')
newsheet = joined.to_csv(path_or_buf=filename, columns=["productcode","productprice"], index=False)