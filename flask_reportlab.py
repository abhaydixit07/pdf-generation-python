from flask import Flask, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

def create_pdf():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Set up the heading
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "This is the Heading")
    
    # Set up the content
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, "This is the content that follows the heading. It provides more detailed information.")
    
    c.save()
    buffer.seek(0)
    return buffer

@app.route('/download-pdf')
def download_pdf():
    pdf = create_pdf()
    return send_file(pdf, as_attachment=True, download_name="example_reportlab.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
