# -*- coding: utf-8 -*-
import PyPDF2
import logging
logging.basicConfig(format='%(asctime)s %(message)s')



def getPDFFormsJSON(fileName):
    logging.warning ("getPDFFormsJSON with " + fileName + " invoked")

    document = PyPDF2.PdfFileReader(fileName)
    documentData = document.getFormTextFields()
    logging.warning(documentData)
    return (documentData)


result = getPDFFormsJSON('Testfiles/KI.pdf')
print (result)