import functions
import numpy as np
from language import max_letters, language_tags
import pandas as pd
import config


word_data = []
language_data = []
master_dic = []
count = 0

#this function is used to generate dictionary for words in german and english language, and produces a final csv
#which contains each word transformed into a vector and its label.
for tag in config.language_tags.keys():
    print('generating dictionary for ' + tag)
    dic = functions.create_df(tag,max_letters)
    for word in dic:
        master_dic.append(word)
    vct = functions.convert_dic_to_vector(dic, max_letters)
    for vector in vct:
        word_data.append(vector)
    output_vct = functions.create_output_vector(count, len(language_tags))
    for i in range(len(vct)):
        language_data.append(output_vct)
    count += 1


arr = []
for i in range(len(word_data)):
    entry = []
    entry.append(master_dic[i])
    for digit in language_data[i]:
        entry.append(float(digit))
    for digit in word_data[i]:
        entry.append(float(digit))
    arr.append(entry)



df_middle = []
arr = np.array(arr)
#np.save('arr.npy', arr)
df=pd.DataFrame(arr)
for i in range(0,len(df)-1):
    df_middle.append(df.iloc[i][0])

df_final = pd.DataFrame(df_middle)
#arr_final = df_final.values
#np.save('arr_final.npy', arr_final)
df_final.to_csv('data_final_2.csv')

