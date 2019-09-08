import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
from language import language_tags, max_letters
import pandas as pd
import config

data = pd.read_csv('data_final_2.csv')
#data = np.load('arr_2.npy',allow_pickle=True)
data_clean = data.dropna(axis='columns')
data_final = data_clean.drop(['Unnamed: 0'], axis=1)
data_np = data_final.values
#seperate vectorized words from labels
inputs = data_np[:, 2:len(data_np[0])]
labels = data_np[:, 0:2]
#split train and test set
x_train, x_test, y_train, y_test = train_test_split(inputs, labels, test_size=0.15)

print(x_test.shape)
print(y_test.shape)
print(x_train.shape)
print(y_train.shape)


#definr input layer, hidden and output layers
network = Sequential()
network.add(Dense(200, input_dim=468, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(2, activation='softmax')) #len(language_tags)

network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

filepath = "weights_8.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
tboard = TensorBoard(log_dir='./logs', write_graph=True, write_images=True)
callbacks_list = [checkpoint, tboard]
#fit the model
network.fit(x_train, y_train, epochs=1000, batch_size=1000, validation_data=(x_test, y_test), callbacks=callbacks_list)

#run tensorboard
#python path_to_tensorboard\main.py --logdir=path_to_AUEB_Invoicer\logs
#then localhost:6006 in a browser