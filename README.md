# LED Price Update Script
This purpose of this program is to generate a .csv with updated product prices to be uploaded to the ecommerce site. You will need a list of current prices and a new price sheet for it to work. It works by merging data from existing price sheets and new price sheets. Currently, this program will only update records where the SKU or product code on the new price sheet exactly matches that of the existing price sheet. 

## Getting Started

Running the program requires installing Python along with several packages
-Python 3: https://www.python.org/download/releases/3.0/
  
  -I used Python version 3.7.2 when creating this program
  
-The following Python packages: os, tkinter, pandas, time

-Instructions on installing a python package: https://packaging.python.org/tutorials/installing-packages/

## Preparing Data for use

In most cases, you will need to do some cleaning of the data before the program can be run.

-Convert price sheet to .csv

-header row must be on the first line of the file

-all relevant headers must be in the same row


## Running the Program

-The full program is called pandafull.py

-Before you begin, download the current listings from the website as a .csv and the new price sheet as .csv. FILES MUST BE IN .CSV FORMAT!!! Convert any .xlsx files to .csv before running. 

-Open the Windows command line and navigate to the folder where you downloaded pandasfull.py

-Type pandasfull.py and hit enter to begin the program

-The program will give prompts when information is needed to join the two .csv files and mark the prices up accordingly

-The program creates two files 'updated' and 'not_updated'
  
  -the 'updated' file can be immediately uploaded to the website; the price has been marked up based on the information you entered earlier in the program. keep in mind only SKUs included on the sheet will be updated. this program will not update prices for options or adders.
  
  -the 'not_updated' file is generated for you to keep track of listings that still need to be worked on
  
  ## Future Improvements
  
  This program is a work-in-progress. I am working on implementing these improvements in the future
  
  -Identify which prices have changed and which have not. Currently the 'updated' .csv that the program outputs contains all matches, including those whose price did not change. I'd like the 'updated' .csv to contain only listings that have changed. This way the user will not have to search the full list for price changes on adders. 


