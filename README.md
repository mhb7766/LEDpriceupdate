# LED Price Update Script
This purpose of this program is to generate a .csv with updated product prices to be uploaded to the ecommerce site. You will need a list of current prices and a new price sheet for it to work. It works by merging data from existing price sheets and new price sheets. Currently, this program will only update records where the SKU or product code on the new price sheet exactly matches that of the existing price sheet. 

Getting Started

Running the program requires installing Python along with several packages
-Python 3: https://www.python.org/download/releases/3.0/
  -I used Python version 3.7.2 when creating this program
  
-The following Python packages: os, tkinter, pandas, time

-Instructions on installing a python package: https://packaging.python.org/tutorials/installing-packages/


Running the Program

-The full program is called pandafull.py

-Before you begin, download the current listings from the website as a .csv and the new price sheet as .csv 

-Open the Windows command line and navigate to the folder where you downloaded pandasfull.py

-Type pandasfull.py and hit enter to begin the program

-The program will give prompts when information is needed to join the two .csv files and mark the prices up accordingly

-The program creates two files 'updated' and 'not_updated'
  
  -the 'updated' file can be immediately uploaded to the website; the price has been marked up based on the information you entered earlier in the program. keep in mind only SKUs included on the sheet will be updated. this program will not update prices for options or adders.
  
  -the 'not_updated' file is generated for you to keep track of listings that still need to be worked on


