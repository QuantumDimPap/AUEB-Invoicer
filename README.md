# AUEB-Invoicer
AUEB Invoicer is an experimental application that can be used to process invoices and also have a monitoring of the whole process. It was developed in the context of the course Big Data Content Analytics over the spring semester of 2019.

AUEB Invoicer developed by:

* Aggeliki Kyrgiou (Operatations and Automation Engineer)
* Antonis Kwnstantinidis (Business Analyst)
* Dimitris Papadoulis (Data Scientist)

# Installation

In order to run the application the following libraries should be installed. Keep in mind that we use Python 3.7.3. You can either choose to download the JetBrain's Pycharm and install all the libraries from inside Pycharm, or pip install them by opening your terminal or command line.

Let's now see, which libraries should be installed, in order the application to work:

* Pandas
* numpy
* tflearn
* keras
* tensorfolw
* email-to
* flask
* wand (Magick Wand) and PIL
* CV2 for image processing
* SMTPLib (it is already a basic package in python 3)
* unidecode (in order to convert words to the same ASCII format)
* Selenium (for web scrapping)
* Scikit learn
* pytesseract (Google's API recognize characters in an image)
* PyPDF for pdf manipulation

After successfully installing the above via pip install or from Pycharm, we can open a terminal and type:

`cd path_that_you_have_downoaded_the_repository/AUEB_Invoicer`

and then type `python app.py`. After that, you should be able to see something like this:

![alt text](https://github.com/QuantumDimPap/AUEB-Invoicer/blob/master/images/terminal_image.PNG)

After that you should copy the http adress that is given and paste it in any browser you want. (we tested Chrome and Firefox)
After that you should be able to see something like this:

![alt text](https://github.com/QuantumDimPap/AUEB-Invoicer/blob/master/images/AUEB%20Invoicer_home.PNG)

After that you can upload an invoice and see the results.

Please keep in mind, due to the fact that the invoices we have gathered are confidential, we kept only two testing invoices in case you want to try the model. You should remember to adjust the file paths accordingly into the scripts provided. Unzip, what has to be unzipped.

Keep the Uploads folder empty.

Also in the script `email_functions.py`, you should put your own credentials.

Finally, the models that we developed using neural networks, were two:

* Convolutional neural networks for image classification
* Faced forward neural networks for language recognition

Both of them are already trained and we have provided the files where they are saved.

If you then want to run Tensorboard to see the graphs that are produced after running the application logs (or the ones attached here), that provide the accuracy and the structure of each model head in the terminal and type (provided that you are located into the folder AUEB Invoicer):

`python path_to_tensorboard\main.py --logdir= path_to_AUEB_Invoicer\logs` for the language prediction model

`python path_to_tensorboard\main.py --logdir= path_to_AUEB_Invoicer\log` for the image classification model

Then head to the browser and type: `localhost:6006` and you should be able to see something like this:

![alt text](https://github.com/QuantumDimPap/AUEB-Invoicer/blob/master/images/tensorboard.PNG)

The whole process described above, automated with BluePrism. 

![alt text](https://github.com/QuantumDimPap/AUEB-Invoicer/blob/master/images/blueprism-logo.png)


If you encounter any problems running the application, do not hesitate to contact us:

email: papadoulis.dimitrios@gmail.com

mobile: +30 6971808435
