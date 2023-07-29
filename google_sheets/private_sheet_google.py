"""
This python module introduces the method to handling  private google sheets.
"""
import gspread

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
data = worksheet2.get_all_records()
print(data[10])