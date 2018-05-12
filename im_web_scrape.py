# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import pandas as pd
import sys


# specify the url
im_page = "http://www.ironman.com/triathlon/events/americas/ironman/world-championship/results.aspx"

from urllib.request import urlopen
page = urllib.urlopen(im_page)
soup = BeautifulSoup(page, 'lxml')        #parse html
#name_box = soup.find('tr', attrs={'class': 'odd'})

table = soup.find_all('table')[0] # Grab the first table

n_columns = 0
n_rows=0
column_names = []

# Find the number of rows and columns
for row in table.find_all('tr'):
    # Determine the number of rows in the table
    td_tags = row.find_all('td')
    if len(td_tags) > 0:
        n_rows+=1
        if n_columns == 0:
            # Set the number of columns for our table
            n_columns = len(td_tags)

    # Handle column names if we find them
    th_tags = row.find_all('th')
    if len(th_tags) > 0 and len(column_names) == 0:
        for th in th_tags:
            column_names.append(th.get_text())

# Error checking for Column Names
if len(column_names) > 0 and len(column_names) != n_columns:
    raise Exception("The column titles do not match the number of columns")

columns = column_names if len(column_names) > 0 else range(0,n_columns)
new_table = pd.DataFrame(columns=columns, index= range(0,n_rows))

row_marker = 0
for row in table.find_all('tr'):
    #print(row)
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        #print(column.get_text())
        #print("ROW: {}   COL: {}".format(row_marker, column_marker))
        new_table.iat[row_marker,column_marker] = column.get_text()
        column_marker += 1
    if len(columns) > 0:
        row_marker += 1

print(new_table)
