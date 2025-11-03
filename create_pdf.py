#!/usr/bin/env python3
"""
Script untuk membuat PDF dari file C++
"""

# Membuat PDF sederhana menggunakan HTML dan kemudian konversi
# Atau menggunakan library yang tersedia

import sys

# Coba import reportlab, jika tidak ada gunakan alternatif
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
    from reportlab.lib.enums import TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("ReportLab tidak tersedia, akan menggunakan metode alternatif...")

def create_pdf_with_reportlab(input_file, output_file):
    """Membuat PDF menggunakan ReportLab"""
    # Baca konten file C++
    with open(input_file, 'r', encoding='utf-8') as f:
        cpp_content = f.read()
    
    # Buat PDF
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Judul
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor='#333333',
        spaceAfter=30,
        alignment=TA_LEFT
    )
    
    title = Paragraph("KARINA MAYSA AMANDA - Program C++", title_style)
    story.append(title)
    story.append(Spacer(1, 0.2*inch))
    
    # Deskripsi
    desc_text = "Program C++ untuk operasi matematika menggunakan array"
    desc = Paragraph(desc_text, styles['Normal'])
    story.append(desc)
    story.append(Spacer(1, 0.3*inch))
    
    # Kode C++
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        fontName='Courier'
    )
    
    code_title = Paragraph("<b>Source Code:</b>", styles['Heading2'])
    story.append(code_title)
    story.append(Spacer(1, 0.1*inch))
    
    # Preformatted untuk kode
    code = Preformatted(cpp_content, code_style)
    story.append(code)
    
    # Build PDF
    doc.build(story)
    print(f"PDF berhasil dibuat: {output_file}")

def create_pdf_with_html(input_file, output_file):
    """Membuat PDF menggunakan HTML sebagai alternatif"""
    # Baca konten file C++
    with open(input_file, 'r', encoding='utf-8') as f:
        cpp_content = f.read()
    
    # Escape HTML characters
    cpp_content = cpp_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Buat HTML
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>KARINA MAYSA AMANDA - Program C++</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
        }}
        .description {{
            background-color: #f4f4f4;
            padding: 15px;
            border-left: 4px solid #333;
            margin: 20px 0;
        }}
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 15px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.4;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            color: #888;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <h1>KARINA MAYSA AMANDA</h1>
    <h2>Program C++ - Operasi Array</h2>
    
    <div class="description">
        <p><strong>Deskripsi:</strong> Program C++ untuk melakukan operasi matematika (penjumlahan, pengurangan, dan perkalian) menggunakan array.</p>
        <p><strong>File:</strong> KARINA MAYSA AMANDA_11-11.cpp</p>
    </div>
    
    <h2>Source Code</h2>
    <pre>{cpp_content}</pre>
    
    <div class="footer">
        <p>Dokumen dibuat secara otomatis</p>
    </div>
</body>
</html>"""
    
    # Simpan HTML
    html_file = output_file.replace('.pdf', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML berhasil dibuat: {html_file}")
    print("Untuk mengkonversi ke PDF, Anda bisa:")
    print("1. Buka file HTML di browser dan print to PDF")
    print("2. Gunakan wkhtmltopdf: wkhtmltopdf input.html output.pdf")
    print("3. Gunakan Chrome headless: chrome --headless --print-to-pdf=output.pdf input.html")

if __name__ == "__main__":
    input_file = "/vercel/sandbox/KARINA MAYSA AMANDA_11-11.cpp"
    output_file = "/vercel/sandbox/KARINA_MAYSA_AMANDA.pdf"
    
    if REPORTLAB_AVAILABLE:
        create_pdf_with_reportlab(input_file, output_file)
    else:
        create_pdf_with_html(input_file, output_file)
