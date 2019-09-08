from PyPDF2 import PdfFileWriter, PdfFileReader
from wand.image import Image as wi
import os
#this script can be used if you want to process the invoices you have and pass them as input in the models


##############################################################################################################################
#the first part of the code is used to extract only the first page from each invoice
##############################################################################################################################
os.getcwd()
os.chdir("path_to_AUEB_Invoicer/invoices to be used")
languages = os.listdir("path_to_AUEB_Invoicer/invoices to be used/")

for language in languages:
    os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}".format(language))
    customers = os.listdir("path_to_AUEB_Invoicer/invoices to be used/{}".format(language))
    for customer in customers:
        os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}/{}".format(language,customer))
        invoices = os.listdir("path_to_AUEB_Invoicer/invoices to be used/{}/{}".format(language,customer))
        i=0
        for invoice in invoices:
            inputpdf = PdfFileReader(open(invoice, "rb"))
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(0))
            with open("{}_{}.pdf".format(customer,i), "wb") as outputStream:
                output.write(outputStream)

            i=i+1

##########################################################################################
#the second part is used in order to convert the pdf files to jpeg
##########################################################################################

os.getcwd()
os.chdir("path_to_AUEB_Invoicer/AUEB_Invoicer/invoices to be used")
languages = os.listdir("path_to_AUEB_Invoicer/AUEB_Invoicer/invoices to be used/")

for language in languages:
    os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}".format(language))
    customers = os.listdir("path_to_AUEB_Invoicer/invoices to be used/{}".format(language))
    for customer in customers:
        os.chdir("path_to_AUEB_Invoicer/invoices to be used/{}/{}".format(language,customer))
        invoices = os.listdir("path_to_AUEB_Invoicer/invoices to be used/{}/{}".format(language,customer))
        i=0
        for invoice in invoices:
            #pdf = wi('MADISON_0.pdf', resolution=300)
            image_pdf = wi(filename=invoice,resolution=300)
            pdfImage = image_pdf.convert("jpeg")
            jpgImage = wi(image=pdfImage)
            jpgImage.save(filename= '{}_{}'.format(customer,i) +".jpg")
            i = i + 1







