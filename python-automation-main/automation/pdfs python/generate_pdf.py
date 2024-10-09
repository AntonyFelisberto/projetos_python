from fpdf import FPDF

pdf = FPDF(orientation="P",unit="pt",format="A4")
pdf.add_page()

pdf.image("automation\\pdfs python\\files\\tiger (1).jpeg",w=0,h=50)#,x=500

pdf.set_font(family="Times",style="B",size=24)
pdf.cell(w=0,h=50,txt="Malayalam Tiger",align="C",border=1,ln=1)

pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=0,h=15,txt="Description",ln=1)

pdf.set_font(family="Times",size=12)
txt = """The tiger (Panthera tigris) is the largest living cat species and a member of the genus Panthera. It is most recognisable for its dark vertical stripes on orange fur with a white underside. An apex predator, it primarily preys on ungulates, such as deer and wild boar. It is territorial and generally a solitary but social predator, requiring large contiguous areas of habitat to support its requirements for prey and rearing of its offspring. Tiger cubs stay with their mother for about two years and then become independent, leaving their mother's home range to establish their own."""
pdf.multi_cell(w=0,h=15,txt=txt)

pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=100,h=25,txt="Kingdom: ")

pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=100,h=25,txt="Animalia",ln=1)

pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=100,h=25,txt="Phylum: ")

pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=100,h=25,txt="Chordata",ln=1)

pdf.output("output.pdf")