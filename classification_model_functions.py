#the packages we are gonna use for developing our model are:
import cv2 #for image manipulation
import numpy as np #for arrays
import os
from random import shuffle

#function for labeling an image
def label_img(tag):
    
    if tag == 'KARAMIKOLA' : return [1,0,0,0,0]
    elif tag == 'OTE' : return [0,1,0,0,0]
    elif tag == 'Technicomer' : return [0,0,1,0,0]
    elif tag == 'MADISON' : return [0,0,0,1,0]
    elif tag == 'HELLO WORLD' : return [0,0,0,0,1]


def create_training_data(img_size):
    training_data = []
    os.chdir("path_to_AUEB_Invoicer/invoices to be used")
    lang_tags = os.listdir()
    for tag in lang_tags:
        os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}".format(tag))
        os.getcwd()
        customers = os.listdir()
        for customer in customers:
            os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}/{}".format(tag,customer))
            images = os.listdir()
            label = label_img(customer)
            for img in images:
                try:
                    cv_image = cv2.resize(cv2.imread("path_to_AUEB_Invoicer/invoices to be used/{}/{}/{}".format(tag,customer,img),cv2.IMREAD_GRAYSCALE),(img_size,img_size))
                    training_data.append([np.array(cv_image),np.array(label)])
                except Exception as e:
                    continue
    shuffle(training_data)
    os.chdir("path_toAUEB_Invoicer/invoices to be used")
    np.save("train_data.npy",training_data)
    return training_data


