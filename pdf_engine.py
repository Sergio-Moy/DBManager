from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog
from io import BytesIO

image = 'assets\logo.png' 

def createpdf(client):
    buffer = BytesIO()
    w,h = A4
    c = canvas.Canvas(buffer, pagesize=A4)
    c.drawImage(image, 50, h-50, 50, 50, mask='auto')
    c.drawString(50, h - 100, f"Estimado cliente {client}")
    c.drawString(50, h - 150, "Esta es una cotización de prueba")
    c.save()
    buffer.seek(0)
    content = buffer.getvalue()

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(

        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        title="Save PDF as"
    )
    with open(file_path, "wb") as file:
        file.write(content)
    return 0