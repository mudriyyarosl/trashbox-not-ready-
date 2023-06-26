from reportlab.pdfgen import canvas

def create_pdf_from_text(text_file, output_pdf):
    # Create a new PDF document
    c = canvas.Canvas(output_pdf)

    # Read the text from the file
    with open(text_file, 'r') as file:
        text = file.read()

    # Set font and size for the text
    c.setFont("Helvetica", 12)

    # Set the position for the text on the page (adjust as needed)
    x = 50
    y = 700

    # Split the text into lines and write them on the PDF
    lines = text.split('\n')
    for line in lines:
        c.drawString(x, y, line)
        y -= 15

    # Save the PDF document
    c.save()

# Example usage
text_file_path = 'input.txt'  # Replace with your text file path
pdf_file_path = 'output.pdf'  # Replace with your desired output PDF file path

create_pdf_from_text(text_file_path, pdf_file_path)
