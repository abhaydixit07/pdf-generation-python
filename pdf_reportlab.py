from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Set up the heading
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "This is the Heading")
    
    # Set up the content
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, "This is the content that follows the heading. It provides more detailed information.")
    
    c.save()

create_pdf("example_reportlab.pdf")
