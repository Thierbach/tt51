from pikepdf import Pdf
import magic
import logging
logging.basicConfig(format='%(asctime)s %(message)s')

# Diese Funktion ermittelt den Typ eines PDF Dokuments und überprüft, ob es PDF/A konform ist
def checkPDFType(fileName):
    logging.warning ("checkPDFType with " + fileName + " invoked")

    # new_pdf = Pdf.new()
    with Pdf.open(fileName) as pdf:
        meta = pdf.open_metadata()
        pdf_format = meta.pdfa_status
        if pdf_format == "":
            logging.warning('PDF is not compliant with PDF/A standard')
            return (magic.from_file(fileName))
        else:
            logging.warning ('PDF is compliant with PDF/A standard')
            logging.warning ('PDF is ' + pdf_format)
            return (pdf_format)

"""
Testcase
bild2.pdf           PDF document, version 1.3
neu0040-A2-b.pdf    PDF is compliant with PDF/A standard / PDF is 2B
GLS.pdf             PDF is compliant with PDF/A standard / PDF is 1A
scan0033.pdf        PDF document, version 1.4
""" 


"""
files = ["Testfiles/bild2.pdf", "Testfiles/neu0040-A2-b.pdf", "Testfiles/GLS.pdf", "Testfiles/scan0033.pdf"]
for fileName in files:
    response = checkPDFType(fileName)
    print (fileName + " : " + response)
"""    
    
    