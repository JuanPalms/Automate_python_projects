"""
This python module develops more complex operations on Google Sheets.
"""
import gspread
import statistics

# Establish connection to Google Sheets
gc = gspread.service_account(filename='google_keys.json')

# Getthe spreadsheet
spreadsheet = gc.open('python_exercise')

worksheet = spreadsheet.worksheet('2013')

# Change the temperature values from Celsius to Fahrenheit
celsius_column = worksheet.get_values('E2:E25')

new_farenheit_column = [ [round(float(i[0])*9/5 + 32, 1)]  for i in celsius_column]

# update the values in the spreadsheet
worksheet.update('G1:G25', [['Fahrenheit']]+ new_farenheit_column)


# Get the mean of the temperature values
farenheit_column = worksheet.get_values('G2:G25')

flat_farenheit_column = [float(i[0]) for i in farenheit_column]

mean = statistics.mean(flat_farenheit_column)

worksheet.update('G26', [[mean]])
