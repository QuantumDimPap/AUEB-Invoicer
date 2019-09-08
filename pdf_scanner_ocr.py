import os
import pandas as pd
from PIL import Image
from wand.image import Image as wi
import pytesseract

def OCR(file,lang):

    #convert to text
    im = Image.open('path_to_AUEB_Invoicer\\Uploads\\{}'.format(file)) #testing invoices
    text = pytesseract.image_to_string(im,lang = lang) #Greek #eng_2 #deu #ell

    return text