import pathlib
from pdf2image import convert_from_path
import PyPDF2

def get_pdf_page_number(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as fh:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(fh)
        # Get the number of pages
        num_pages = len(pdf_reader.pages)
        return num_pages



folder=pathlib.Path(r"/var/datasets/izohli_lugat")
file="uzbek_tilining_izohli_lugati_t_www.ziyouz.com.pdf"
print(f"will process {file}, exists : {(folder/file).exists()}")

img_folder=folder/"images"
if not img_folder.exists():
    img_folder.mkdir(parents=True)


pdf_page_numb=get_pdf_page_number(folder/file)
counter=1
one_time_read_pages=100
first_pages=[i*one_time_read_pages for i in range(pdf_page_numb//one_time_read_pages)]
last_pages = [(i+1)*one_time_read_pages for i in range(pdf_page_numb//one_time_read_pages)]
for read_round,(first_page,last_page) in enumerate(zip(first_pages,last_pages)):
    images = convert_from_path(folder/file,first_page=first_page,last_page=last_page)
    print(f"converted {len(images)} pages")

    for i,img in enumerate(images):
        img.save(img_folder/f"t_harfi_{read_round}_{i}.jpg","JPEG")
    answer=input("coninue?")
    if answer.lower() in ["yes","y"]:
        continue
    else:
        break