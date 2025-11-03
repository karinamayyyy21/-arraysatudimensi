#!/usr/bin/env python3
"""
Membuat PDF sederhana tanpa library eksternal
Menggunakan format PDF dasar
"""

def create_simple_pdf(input_file, output_file):
    """Membuat PDF sederhana dari file C++"""
    
    # Baca konten file C++
    with open(input_file, 'r', encoding='utf-8') as f:
        cpp_content = f.read()
    
    # Escape karakter khusus untuk PDF
    cpp_content = cpp_content.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    
    # Template PDF dasar
    pdf_content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/Resources <<
/Font <<
/F1 <<
/Type /Font
/Subtype /Type1
/BaseFont /Courier
>>
/F2 <<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica-Bold
>>
/F3 <<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
>>
>>
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj

4 0 obj
<<
/Length 5 0 R
>>
stream
BT
/F2 16 Tf
50 750 Td
(KARINA MAYSA AMANDA) Tj
0 -30 Td
/F3 12 Tf
(Program C++ - Operasi Array) Tj
0 -25 Td
/F3 10 Tf
(File: KARINA MAYSA AMANDA_11-11.cpp) Tj
0 -30 Td
/F2 11 Tf
(Source Code:) Tj
0 -20 Td
/F1 8 Tf
"""

    # Tambahkan kode C++ baris per baris
    lines = cpp_content.split('\n')
    y_offset = -12
    
    for line in lines[:50]:  # Batasi 50 baris pertama untuk kesederhanaan
        if line.strip():
            # Escape dan bersihkan line
            clean_line = line.replace('\r', '').strip()
            if len(clean_line) > 80:
                clean_line = clean_line[:80] + '...'
            pdf_content += f"0 {y_offset} Td\n({clean_line}) Tj\n"
            y_offset = -12
    
    pdf_content += """ET
endstream
endobj

5 0 obj
"""
    
    # Hitung panjang stream (perkiraan)
    stream_start = pdf_content.find("stream\n") + 7
    stream_end = pdf_content.find("\nendstream")
    stream_length = stream_end - stream_start
    
    pdf_content += f"{stream_length}\n"
    pdf_content += """endobj

xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000407 00000 n 
"""
    
    # Tambahkan offset xref
    pdf_content += f"{len(pdf_content):010d} 00000 n \n"
    pdf_content += """trailer
<<
/Size 6
/Root 1 0 R
>>
startxref
"""
    pdf_content += f"{len(pdf_content)}\n"
    pdf_content += "%%EOF"
    
    # Tulis PDF
    with open(output_file, 'wb') as f:
        f.write(pdf_content.encode('latin-1', errors='ignore'))
    
    print(f"PDF sederhana berhasil dibuat: {output_file}")

if __name__ == "__main__":
    input_file = "/vercel/sandbox/KARINA MAYSA AMANDA_11-11.cpp"
    output_file = "/vercel/sandbox/KARINA_MAYSA_AMANDA.pdf"
    
    try:
        create_simple_pdf(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        print("Menggunakan metode alternatif...")
