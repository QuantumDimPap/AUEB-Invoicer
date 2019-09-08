#import necessary packages

import re
import os
import numpy as np
import pandas as pd
from wand.image import Image as wi
import pytesseract
from PIL import Image
import pdf_scanner_ocr
import classification_model



#technicomer
def regex_technicomer():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg','Greek')
    #convert to lowercase
    text = text.lower()
    #remove \n (new lines)
    text = text.replace('\n','')
    #replace space with commas
    text=text.replace(' ',',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')

    text_VAT = re.search(r'αφμ,(.*?)7δ\.ο\.υ,', text).group(1)  # in Greece VAT number is 9 digits
    company = 'Technicomer'
    payment = re.search(r'επληρώτεο,(.*?),ε,πληρωτεο,την,', text).group(1)
    has_to_be_paid_until = re.search(r'πληρωτεο,την,(.*?),αρ.λογαριασμων,/', text).group(1)


    results_list = [text_VAT,company,payment,has_to_be_paid_until]

    return results_list

#hello world
def regex_HELLOWORLD(language_tag):
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg',language_tag)
    #convert to lowercase
    text = text.lower()
    #remove \n (new lines)
    text = text.replace('\n','')
    #replace space with commas
    text=text.replace(' ',',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')

    text_VAT = re.search(r'road,po,(.*?)\(123\),456,', text).group(1)
    company = 'HELLO WORLD'
    payment = re.search(r'00total,(.*?)many,thanks,for,', text).group(1)
    has_to_be_paid_until = re.search(r'to,be,received,within,(.*?),days.powered,by', text).group(1) + ' days' + ' from ' + re.search(r'hello,world,invoice123,southwest,(.*?)silicon,valley,', text).group(1)



    results_list = [text_VAT,company,payment,has_to_be_paid_until]

    return results_list


#OTE
def regex_OTE():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg','ell') #ell for OTE
    #convert to lowercase
    text = text.lower()
    #remove \n (new lines)
    text = text.replace('\n','')
    #replace space with commas
    text=text.replace(' ',',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')

    text_VAT = re.search(r'αφμ,(.*?),δου,', text).group(1)
    text_VAT = text_VAT[0:9]
    company = 'OTE'
    payment = re.search(r',λογαριασμού,\(µε,φπα\),(.*?)εποσό,πληρωμής,', text).group(1)
    payment = payment.replace(',','.')
    payment = str(np.round(float(payment),decimals=2))
    has_to_be_paid_until = re.search(r'ις,-30,0970ε(.*?)σας,ευχαριστούμεσύνολο,', text).group(1)


    results_list = [text_VAT,company,payment,has_to_be_paid_until]

    return results_list


#madison
def regex_MADISON(language_tag):
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg',language_tag)

    #convert to lowercase
    text = text.lower()
    #remove \n (new lines)
    text = text.replace('\n','')
    #replace space with commas
    text = text.replace(' ',',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')


    text_VAT = re.search(r'vat,de(.*?)unterschrift,', text).group(1)
    text_VAT = text_VAT.replace(',','')
    company = 'MADISON'
    payment = re.search(r'eur,total,(.*?)total,', text).group(1)
    payment = pd.unique(payment.split(','))[0]
    has_to_be_paid_until = '60' + ' days' + ' from ' + re.search(r'datum,(.*?),abreise', text).group(1)
    results_list = [text_VAT,company,payment,has_to_be_paid_until]
    return results_list



def get_clean_text_OTE():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg', 'ell')
    # convert to lowercase
    text = text.lower()
    # remove \n (new lines)
    text = text.replace('\n', '')
    # replace space with commas
    text = text.replace(' ', ',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')
    return text


def get_clean_text_MADISON():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg', 'eng')
    # convert to lowercase
    text = text.lower()
    # remove \n (new lines)
    text = text.replace('\n', '')
    # replace space with commas
    text = text.replace(' ', ',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')
    return text


def get_clean_text_HELLOWORLD():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg', 'eng_2')
    # convert to lowercase
    text = text.lower()
    # remove \n (new lines)
    text = text.replace('\n', '')
    # replace space with commas
    text = text.replace(' ', ',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')
    return text

def get_clean_text_Technicomer():
    text = pdf_scanner_ocr.OCR('PDF_TEST.jpg', 'ell')
    # convert to lowercase
    text = text.lower()
    # remove \n (new lines)
    text = text.replace('\n', '')
    # replace space with commas
    text = text.replace(' ', ',')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(':,', ',')
    text = text.replace(',.', ',')
    text = text.replace('.,', ',')
    text = text.replace(',,', ',')
    return text
