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



def prediction_language(text_input):
    text = re.sub(r'[:^\[\]#)(!>`?+.oo;*§=|"\-/\\\\]', ',', text_input)
    text = ','.join(s for s in text.split(',') if not any(c.isdigit() for c in s))
    text = re.sub(r'[:^\[\]#()!>`?+.oo;*§=|"\-/\\\\]',',',text)
    text = text.replace('‘zimmer', 'zimmer')
    text = text.replace('—,————————mwst',',')
    text = text.replace('@', '')
    text = text.replace(',,,,', ',')
    text = text.replace(',,,', ',')
    text = text.replace(',,', ',')
    text = text.replace(',', ',')
    text = text.replace('----------------', ',')
    text = text.replace(',,,,,,', ',')
    text_list = text.split(',')
    text_list = [item for item in text_list if len(str(item)) <= 18 and len(str(item)) >3]
    #unicode characters
    text_list = [unidecode(item) for item in text_list]

    #init prediction
    network = Sequential()
    network.add(Dense(200, input_dim=468, activation='sigmoid'))
    network.add(Dense(150, activation='sigmoid'))
    network.add(Dense(100, activation='sigmoid'))
    network.add(Dense(100, activation='sigmoid'))
    network.add(Dense(2, activation='softmax'))
    network.load_weights('path_to_AUEB_Invoicer\\weights_8.hdf5')
    network.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

    #prediction of language in the text
    eng_dic = []
    deu_dic = []


    for word in text_list:
        dic = []
        dic.append(word)
        vct_str = network_test.convert_dic_to_vector(dic, max_letters - 1)
        vct = np.zeros((1, 468))
        count = 0
        for digit in vct_str[0]:
            vct[0, count] = int(digit)
            count += 1
        prediction_vct = network.predict(vct)

        langs = list(language_tags.keys())
        for i in range(len(language_tags)):
            lang = langs[i]
            score = prediction_vct[0][i]
            print(lang + ': ' + str(round(100 * score, 2)) + '%')
            if lang == 'en':
                eng_dic.append(score)
            elif lang == 'de':
                deu_dic.append(score)

    #Evaluate Overall, actually here we sum up each percentage has gathered in eng_dic and deu_dic and in that way
    #we can decide which language represents the text.
    if sum(deu_dic) > sum(eng_dic):
        language_of_text = 'deu'
    else:
        language_of_text = 'eng_2'

    return language_of_text