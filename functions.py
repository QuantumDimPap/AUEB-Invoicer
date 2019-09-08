import re
#import wikipedia as wiki
from unidecode import unidecode
import language
import pandas as pd
import os
import config
import random

final_list = []

'''
First try was to gather data from wikipedia but this did not work quite as expected.

def generate_dictionary(tag, max_word_length):

    wiki.set_lang(tag)
    for topic in config.language_tags[tag]:
        page = wiki.WikipediaPage(topic)
        content = page.content
        content = unidecode(content)
        lst = process(content, max_word_length)
    return lst
'''

def process(page_content, max_word_length):
    words = re.sub(r'[^a-zA-Z ]', '', page_content)
    lower = words.lower()
    word_list = lower.split()
    short_words = []
    for word in word_list:
        if len(word) <= max_word_length:
            short_words.append(word)
    return short_words

#creates dataframe with each word either in english or german
def create_df(tag_words,max_words):
    df = pd.read_csv('path_to_AUEB_Invoicer/language_model/{}.txt'.format(tag_words), header=None)
    df = df.sample(n=150000,replace="False")
    #print(df.shape)
    df = df.astype(str)
    df_list = df.iloc[:, 0].tolist()
    #df_list = df_list.sample(n=50000, replace="False")
    df_list = [item for item in df_list if len(str(item)) <= max_words]
    df_list = [item.lower() for item in df_list]
    return df_list

#converts each word to a number and then to a vector
def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word)
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec +str(0)*26*excess
        new_list.append(vec)
    print(len(new_list))
    return new_list

def create_output_vector(tag_index, number_of_languages):
    out = str(0)*tag_index + str(1) + str(0)*(number_of_languages-1-tag_index)
    return out