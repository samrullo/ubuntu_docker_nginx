import os
import pathlib
from PIL import Image
import pytesseract

folder = pathlib.Path(r"/var/datasets/izohli_lugat/images")
img_file="t_harfi_1.jpg"
print(f"About to ocr file {folder/img_file}, exists {(folder/img_file).exists()}")

txt = pytesseract.image_to_string(Image.open(folder/img_file), lang="uzb_cyrl")
print(f"Find OCR processed result : \n {txt}")

ocr_result_folder=pathlib.Path(r"/var/datasets/izohli_lugat/ocr_result")
if not ocr_result_folder.exists():
    ocr_result_folder.mkdir()

ocr_result_file=ocr_result_folder/(img_file+".txt")
ocr_result_file.write_text(txt)