"""
This python module reads tables stored in pdfs
"""
import tabula

table = tabula.read_pdf('encuesta_sf.pdf',pages=6)

print(table)