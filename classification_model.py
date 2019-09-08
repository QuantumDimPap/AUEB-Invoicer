
def prediction(img_name):

    #the packages we are gonna use for developing our model are:
    import cv2 #for image manipulation
    import numpy as np
    import os
    from random import shuffle
    import classification_model_functions
    from PyPDF2 import PdfFileWriter, PdfFileReader
    from wand.image import Image as wi



    image_size = 50
    learning_rate = 1e-3

    #give a name to the model
    model_name = 'invoice_classification - {} - {} model'.format(learning_rate,'2conv-basic')

    #data = classification_model_functions.create_training_data(50)

    train_data = np.load("path_to_AUEB_Invoicer\\invoices to be used\\train_data.npy",allow_pickle=True)

    #the model
    import tflearn
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.core import input_data, dropout, fully_connected
    from tflearn.layers.estimator import regression

    train = train_data[-400:]
    test = train_data[:-400]

    image_size = 50
    learning_rate = 1e-3

    X = np.array([i[0] for i in train]).reshape(-1, image_size,image_size,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1, image_size,image_size,1)
    test_y = [i[1] for i in test]

    convnet = input_data(shape=[None, image_size, image_size, 1], name='input')

    convnet = conv_2d(convnet, 32, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 32, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 32, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)


    convnet = conv_2d(convnet, 32, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)


    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 5, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log')
    #if you do not want to load the model you must first fit the data.
    #model.fit({'input': X}, {'targets': Y}, n_epoch=100, validation_set=({'input': test_x}, {'targets': test_y}),
    #    snapshot_step=50, show_metric=True, run_id='model_name')

    #model.save('AUEB_Invoicer_model')

    model.load("path_to_AUEB_Invoicer\\AUEB_Invoicer_model")


    #prediction


    #take 1st page
    os.chdir('path_to_AUEB_Invoicer/Uploads')
    #testing invoices
    inputpdf = PdfFileReader(open(img_name, "rb"))
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(0))

    with open("{}_TEST.pdf".format('PDF'), "wb") as outputStream:
        output.write(outputStream)
        outputStream.close()
    outputStream.close()
    inputpdf.stream.close()
    #convert to jpeg
    image_pdf = wi(filename="PDF_TEST.pdf",resolution=300)
    pdfImage = image_pdf.convert("jpeg")
    jpgImage = wi(image=pdfImage)
    jpgImage.save(filename= 'PDF_TEST' +".jpg")

    #convert image to array
    cv_image = cv2.resize(cv2.imread("path_to_AUEB_Invoicer\\Uploads\\PDF_TEST.jpg",cv2.IMREAD_GRAYSCALE),(image_size,image_size)) #testing_invoices
    testing_data_final = cv_image.reshape(-1,image_size,image_size,1)

    model_out = model.predict(testing_data_final)
    result = np.argmax(np.round(model_out))

    if result == 0: return 'KARAMIKOLA'
    elif result == 1: return 'OTE'
    elif result == 2: return 'Technicomer'
    elif result == 3: return 'MADISON'
    elif result == 4: return 'HELLO WORLD'




#prediction('0000679498122017.pdf') #madison_484950.pdf

#http://localhost:6006 , for tensorboard