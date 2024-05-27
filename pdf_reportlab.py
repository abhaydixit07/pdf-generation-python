from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Image

def create_pdf(file_path, image_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Set up the heading
    c.setFont("Helvetica-Bold", 18)
    heading_text = "This is the Heading"
    text_width = c.stringWidth(heading_text, "Helvetica-Bold", 18)
    c.drawString((width - text_width) / 2.0, height - 50, heading_text)  # adjust the y-coordinate as needed
    
    # Set up the content
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "This is the content that follows the heading. It provides more detailed information.")  # adjust the y-coordinate as needed
    
    # Add the image
    c.drawImage(image_path, 50, height - 300, width=200, height=200)  # adjust position and size as needed

    c.save()

create_pdf("example_reportlab.pdf", "about.jpg")