"""
This python module implements the data extraction from a pdf with python
"""
import fitz

with fitz.open("encuesta_sf.pdf") as pdf:
    page5=pdf[5].get_text()
    print(page5)
        