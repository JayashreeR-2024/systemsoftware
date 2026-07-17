from reportlab.pdfgen import canvas
from pathlib import Path

Path("test_files").mkdir(exist_ok=True)

# Create valid PDF
pdf_path = "test_files/valid_file.pdf"

c = canvas.Canvas(pdf_path)
c.drawString(100, 750, "Selenium upload test PDF")
c.save()

print("Created:", pdf_path)


# Create invalid file
with open("test_files/invalid_file.exe", "w") as f:
    f.write("This is not a supported upload format")

print("Created invalid file")