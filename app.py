import os
from flask import Flask, request, render_template, url_for, redirect
import random
import re
import os
import numpy as np
import pandas as pd
from wand.image import Image as wi
import pytesseract
from PIL import Image
import pdf_scanner_ocr
import classification_model
import regex_file
from keras.models import Sequential
from keras.layers import Dense
from config import max_letters, language_tags
import numpy as np
from unidecode import unidecode
from language import max_letters,language_tags
import network_test
import main_app
import shutil
import glob
import validating_VAT
import email_functions





app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    # get name
    return render_template("header.html")


@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join('path_to_AUEB_Invoicer/Uploads', photo.filename))
            
            # predict in what category of invoices the incoming invoice belongs
            name = os.listdir('C:/Users/dpapadoulis/Desktop/AUEB_Invoicer/Uploads')
            label = classification_model.prediction(name[0])

            # checking
            if label == 'Technicomer':
                text = regex_file.get_clean_text_Technicomer()
                country_str = "// select[ @ id = 'countryCombobox'] // option[ @ value = 'EL'][contains(text(), 'EL-Ελλάδα')]"
                result = regex_file.regex_technicomer()
                vies = validating_VAT.giveAFM(result[0], "http://ec.europa.eu/taxation_customs/vies/", country_str)
            elif label == "OTE":
                text = regex_file.get_clean_text_OTE()
                country_str = "// select[ @ id = 'countryCombobox'] // option[ @ value = 'EL'][contains(text(), 'EL-Ελλάδα')]"
                result = regex_file.regex_OTE()
                vies = validating_VAT.giveAFM(result[0], "http://ec.europa.eu/taxation_customs/vies/", country_str)
            elif label == "MADISON":
                text = regex_file.get_clean_text_MADISON()
                language_final_tag = main_app.prediction_language(text)
                result = regex_file.regex_MADISON(language_final_tag)
                country_str = "//select[@id='countryCombobox']//option[@value='DE'][contains(text(),'DE-Γερμανία')]"
                vies = validating_VAT.giveAFM(result[0],"http://ec.europa.eu/taxation_customs/vies/",country_str)
            elif label == "HELLO WORLD":
                text = regex_file.get_clean_text_HELLOWORLD()
                country_str = "//select[@id='countryCombobox']//option[@value='DE'][contains(text(),'DE-Γερμανία')]"
                language_final_tag = main_app.prediction_language(text)
                result = regex_file.regex_HELLOWORLD(language_final_tag)
                vies = validating_VAT.giveAFM(result[0], "http://ec.europa.eu/taxation_customs/vies/", country_str)
            elif label == None:
                print("Template not available.")

            #convert to english
            if vies == 'Ναι':
                vies = 'Yes'
            else:
                vies = 'No'

            email_functions.email(result[1],vies)

            files = glob.glob('path_to_AUEB_Invoicer/Uploads/*')
            for f in files:
                os.remove(f)

            return render_template('second.html', company_name=result[1],
                           VAT_Number=result[0],vies_valid=vies,payment=result[2],paid_until=result[3])

        else:
            return redirect(url_for('fileFrontPage'))



if __name__ == '__main__':
    app.run()

#if you want to run from terminal
#cd Desktop/AUEB_Invoicer
#and then
#python app.py