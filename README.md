# AUEB-Invoicer
AUEB Invoicer is an experimental application that can be used to process invoices. It was developed in the context of the course Big Data Content Analytics over the spring semester of 2019.

AUEB Invoicer developed by:

* Aggeliki Kyrgiou (Operatations and Automation Engineer)
* Antwnis Kwnstantinidis (Business Analyst)
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



