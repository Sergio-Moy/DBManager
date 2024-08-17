from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import tkinter as tk
from tkinter import filedialog

image_path = r'assets\logo.png'

def createpdf(client, orden, cot_id):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    logo = Image(image_path)
    logo.drawHeight = 100
    logo.drawWidth = 100
    logo.hAlign = 'LEFT'
    elements.append(logo)

    elements.append(Paragraph(f"Cotización N°{cot_id}", title_style))
    elements.append(Paragraph(f"Estimado cliente {client}", normal_style))
    elements.append(Paragraph("Esta es una cotización de prueba", normal_style))

    table = Table(orden, colWidths=110, rowHeights=30)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#d5a6bd'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#ffffff'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#f4f4f4'),
        ('GRID', (0, 0), (-1, -1), 1, '#000000'),
    ]))
    elements.append(table)

    doc.build(elements)

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
    print(orden)
    return 0