# -*- coding: utf-8 -*-
import PyPDF2
import logging
logging.basicConfig(format='%(asctime)s %(message)s')


# Diese Funkion liefert bei durchsuchbaren PDF Dokumenten die Key:Value Paare als JSON String zurück
def getPDFFormsAsJSON(fileName):
    try:
        logging.warning ("getPDFFormsAsJSON with " + fileName + " invoked")
    
        document = PyPDF2.PdfFileReader(fileName)
        documentData = document.getFormTextFields()
        documentDataRaw = document.getFields()
        logging.warning(documentData)
           
        return (documentData, documentDataRaw)
    except:
        return ("Document Data not resolvable")


result = getPDFFormsAsJSON('Testfiles/KI.pdf')
print (result)