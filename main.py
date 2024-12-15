import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename.title(), ln=1)
    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)



pdf.output("output.pdf")




