import os
import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
#from pathlib import path
import time

#set directory
os.chdir('c:\\users\\mike\\Documents\\led')

#get files
input("Hit enter to choose left table: ")
Tk().withdraw()
l=askopenfilename()

input("Hit enter to choose right table: ")
Tk().withdraw()
r=askopenfilename()

#get key values
l_key = input("Enter key value from left table: ")
r_key = input("Enter key value from right table: ")

#detect delimiter of 'right'
with open(r) as f:
	line = f.readline()

if len(re.split(',',line)) > 1:
	delim = ','
elif len(re.split('\t',line)) > 1:
	delim = '\t'
elif len(re.split(' ',line)) > 1:
	delim = ' '

f.close()

#read datasets
left = pd.read_csv(l, encoding = "ISO-8859-1")
right = pd.read_csv(r, encoding = "ISO-8859-1", sep=delim, engine='python')

#make columns in 'right' dataframe lowercase so input in case insensitive
right.columns = map(str.lower, right.columns)

#remove newline from column names in 'right' dataframe
right.columns = map( lambda s: s.replace('\n',' '), right.columns)

######some edits to match more records########
#replace "/" with "-" in new price sheet to match more records
right[r_key] = right[r_key].str.replace('/', '-')

#use pandas to merge
joined = pd.merge(left, right, how="inner", left_on=l_key, right_on=r_key)

#create unique filename
timestr = time.strftime("%m%d%Y-%H%M%S")
filename = "merged" + timestr + ".csv"

#convert pandas dataframe to .csv and save (keeps only 'productcode and product price')
newsheet = joined.to_csv(path_or_buf=filename, index=False)