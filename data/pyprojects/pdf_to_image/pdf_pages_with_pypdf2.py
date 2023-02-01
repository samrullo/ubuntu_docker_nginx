import PyPDF2
import pathlib

folder=pathlib.Path(r"/var/datasets/izohli_lugat")
file="uzbek_tilining_izohli_lugati_t_www.ziyouz.com.pdf"
print(f"will process {file}, exists : {(folder/file).exists()}")


# Open the PDF file
with open(folder/file, 'rb') as fh:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(fh)
    # Get the number of pages
    num_pages = len(pdf_reader.pages)
    print(num_pages)


# Open the PDF file
with open(folder/file, 'rb') as fh:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(fh)
    # Extract the text from all pages
    for i in range(4):
        page = pdf_reader.pages[i]
        text = page.extract_text()
        print(text)
