from fpdf import FPDF

def main():
    inpName=input("Name : ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(0,60,txt="CS50 Shirtificate",new_x="LMARGIN",new_y="NEXT",align="C")
    pdf.image("shirtificate.png",w=pdf.epw)
    pdf.set_text_color(255,255,255)
    pdf.set_font_size(30)
    pdf.text(x=47.5,y=140,txt=f"{inpName} took CS50")
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()