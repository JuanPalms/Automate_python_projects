"""
This python module shows how to use excel data to produce pdf documents
"""
import os 
import pandas as pd
from fpdf import FPDF

data = pd.read_excel('data.xlsx')

# We need to create one instance for each pdf we want
for index, row in data.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    ### adding title
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
    #attributes = ['kingdom','phylum','class','order','suborder']
    ### adding additional information for each animal
    for column in data.columns: 
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f'{column.title()}:')
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=row[column], ln=1)
        
    pdf.output(f"{row['name']}_information.pdf")