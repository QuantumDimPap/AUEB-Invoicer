from keras.models import Sequential
from keras.layers import Dense
from config import max_letters, language_tags
import numpy as np

#this function coverts each word in the dictionary to a vector taking into account the words used.
def convert_dic_to_vector(lst, max_word_length):
    new_list = []
    for item in lst:
        vec = ''
        n = len(item)
        for x in range(n):
            current_letter = item[x]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec + str(0)*26*excess
        new_list.append(vec)
    # print(len(new_list))
    return new_list


