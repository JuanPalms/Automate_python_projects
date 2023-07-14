"""
This python module creates a simple pdf
"""
from fpdf import FPDF

### Generate a FPDF class object and the pass the arguments
### orientation= {'P':'Portrait'}
### unit ={'pt':'point'}
### 
pdf = FPDF(orientation='P',unit='pt', format='A4')
## adding a new page
pdf.add_page()
#pdf.image('kakashi2.jpg', w=80, h=50)
## add content to the page
### Define the font of the cell
pdf.set_font(family="Times", style="B",size=24)
## adding a title:
## w=0 indicates the cell will take all the space in the page
## h=50 indicates the height of the cell
## align: "C" aling in the center of the page
## ln=1 break line
pdf.cell(w=0, h=20, txt="Kakashi Palmeros", align="C", border=1, ln=1)

### You have to keep adding cells for each text you want to add
pdf.set_font(family="Times",style="B", size=14)
pdf.cell(w=0, h=15, txt="Information", ln = 1)

### Another line
pdf.set_font(family="Times", size=12)
txt_kakashi = """
Kakashi is a Shetland sheepdog born in the state of Georgia, in the United States, on November 10, 2019. Kakashi arrived in Mexico a couple of months after his birth and became part of the Palmeros family on May 20, 2020. Upon his arrival, Kakashi was a somewhat cautious dog who didn't like to interact with his new human family. Gradually, Kakashi adapted to his environment and became part of the family. His first residence was established in the neighborhood of Santa Maria la Ribera, where he began to interact with the world around him. His favorite food is chicken legs, and he enjoys chasing squirrels in the park.
"""
pdf.multi_cell(w=350, h=15, txt=txt_kakashi, align="L")


### give path to the image, give width and heigth try to respect the original ratios
### x,y arguments decide the relative position of the added objects
pdf.image('kakashi.jpg', w=150, h=200, x= 380, y=80)


pdf.set_font(family="Times",style="B", size=14)
pdf.cell(w=60, h=20, txt="Breed:")
pdf.set_font(family="Times", size=14)
pdf.cell(w=60, h=15, txt="Shetland Sheepdog",ln=1)

pdf.set_font(family="Times",style="B", size=14)
pdf.cell(w=60, h=15, txt="Heigt:")
pdf.set_font(family="Times", size=14)
pdf.cell(w=60, h=15, txt="34 cm", ln=1)

pdf.set_font(family="Times",style="B", size=14)
pdf.cell(w=60, h=15, txt="Weigth:")
pdf.set_font(family="Times", size=14)
pdf.cell(w=60, h=15, txt="20kgs", ln=1)




pdf.output('kakashi.pdf')
