import os
import pathlib
from PIL import Image
import pytesseract

folder = pathlib.Path(r"/var/datasets/izohli_lugat/images")
image_files=[file for file in folder.iterdir() if "jpg" in file.suffix]

ocr_result_folder=pathlib.Path(r"/var/datasets/izohli_lugat/ocr_result")
if not ocr_result_folder.exists():
    ocr_result_folder.mkdir(parents=True)

text_part_to_show=200

for i,img_file in enumerate(image_files):
    print(f"Image file {i+1} : About to ocr file {img_file}")

    txt = pytesseract.image_to_string(Image.open(img_file), lang="uzb_cyrl")
    print(f"Find OCR processed result : \n {txt[:text_part_to_show]}")

    ocr_result_filename=img_file.stem+".txt"
    ocr_result_file=ocr_result_folder/ocr_result_filename
    ocr_result_file.write_text(txt)