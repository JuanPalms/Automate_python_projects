"""
This python module introduces the method to handling  private google sheets.
"""
import gspread
import re

# stablish connection with google sheets
gc = gspread.service_account(filename='google_keys.json')

# Get a spreadsheet
spreadsheet = gc.open("python_exercise")
# Specify a sheet by its index
worksheet = spreadsheet.get_worksheet(0)

## get a worksheet by title
worksheet1 = spreadsheet.worksheet("2013")
worksheet2 = spreadsheet.worksheet("2014")

# Get the data from the spreadsheet
complete_data = worksheet2.get_all_records()

## Get a particular row in a given range by cells
single_row = worksheet2.get_values("A5:E5")

## Get a bunch of rows in a given range by cells
many_rows = worksheet2.get_values("A5:E10")


## Getting rows by index
row_index= worksheet2.row_values(3)

## Get a column in a given index
column = worksheet2.col_values(2)[1:]

## Get the value of a single cell
cell_value = worksheet2.cell(2, 2).value
print(cell_value)

## Get the value of a single cell
cell_value = worksheet2.acell('B3').value

## Search for a cell with a value (get the coordinates)
cell = worksheet2.find("10135")

## Search for many cells with a value (get the coordinates)
cells = worksheet2.findall("2014")


## Matchin partial strings
reg=re.compile(r'99')
cells = worksheet2.findall(reg)

for cell in cells:
    print(cell.row, cell.col)

## Update a cell
worksheet2.update('B3', '0')

## Update a cell based on row column
worksheet2.update_cell(5, 2, '0')