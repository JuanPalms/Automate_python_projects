"""
This python module introduces the method to handling  private google sheets.
"""
import gspread

# stablish connection with google sheets
gc = gspread.service_account(filename='google_keys.json')

# Get a spreadsheet by name
spreadsheet = gc.open("python_exercise")
# Specify a sheet by its index
worksheet = spreadsheet.get_worksheet(0)

# Get the data from the spreadsheet
data = worksheet.get_all_records()
print(data[10])