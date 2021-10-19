"""
Paulo Luis 17359
pf1.py and pf2.py
29/08/2021
"""

from reportlab.pdfgen import canvas
import os

#1.a)
def f1(file_name: str):
    c = canvas.Canvas(file_name)
    c.drawString(50, 100, "Bernardo Martinho Marques")
    c.save()
    os.startfile(file_name)
#f1("hello.pdf")

#1.b)
def f2(file_name: str):
    from reportlab.lib.units import mm
    c = canvas.Canvas(file_name)
    c.drawString(8*mm*100, 5*mm*100, "Bernardo Martinho Marques")
    c.setFont("Helvetica", 14)
    c.setFillColorRGB(1,0,0) #choose your font colour
    c.drawString(50, 50, "The quick brown fox jumps over the lazy dog")
    c.setFillColorRGB(0,1,0)
    c.rect(100,100,100, 100, fill=1)
    c.save()
    os.startfile(file_name)
f2("testep1b.pdf", )

#2.a)
def f2_a(file_name):
    from reportlab.lib.pagesizes import A4
    height, width = A4
    c = canvas.Canvas(file_name, pagesize=A4)
    c.drawString(8, 5, "Bernardo Martinho Marques")
    c.setFillColorRGB(1,0,0)
    c.circle(10, height, width, fill=1)
    c.save()
    os.startfile(file_name)
#f2_a("teste2.pdf")