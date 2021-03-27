import textract
from pikepdf import Pdf
import logging
logging.basicConfig(format='%(asctime)s %(message)s')


# Diese Funktion ermittelt, ob ein PDF Dokument durchsuchbar ist.
def checkPDFSeachability(fileName):
    logging.warning ("checkPDFSeachability with " + fileName + " invoked")

    try:
        text = textract.process(fileName, method='pdfminer')  # der Text wird ausgelesen
    
        u = text.decode('utf-8')                # Text wird nach utf-8 konvertiert
        # print (len(u))
        # print (u)
        uWithoutFormFeed = u.replace('\f', '')  # nicht durchsuchbare PDFs haben pro Seite ein Form Feed
                                                # ff werden entfernt  
        # print (len(uWithoutFormFeed))
        if len(uWithoutFormFeed) == 0:          # wenn der Text keine Zeichen enthält, so ist das PDF nicht durchsuchbar
            return ('false')                    # Dokument nicht durchsuchbar
        else:
            return ('true')                     # Dokument ist durchsuchbar
    except:
        return ('false')    

# Diese Funktion ermittelt, ob ein PDF Dokument xmp:Metadata besitzt und liefert das XML Fragment im Erfolgsfall zurück.
def getPDFMetaData(fileName):
    logging.warning ("getPDFMetaData with " + fileName + " invoked")

    #try:
    with Pdf.open(fileName) as pdf:
            xmp = pdf.Root.Metadata.read_bytes()    # xmp-Konten wird gelesen
            type(xmp)                               
            return (xmp.decode("utf-8"))            # xmp-Daten werden als XML Fragment zurückgegeben
    #except:
    #    return ("No xmp:MetaData found")
    

# Diese Funktion liest die Roh-Daten aus einem durchsuchbaren PDF Dokument aus.
def getPDFContent(fileName):
    try:
        logging.warning ("getPDFContent with " + fileName + " invoked")
    
        text = textract.process(fileName, method='pdfminer')
        PDFContent = text.decode('utf8')
        return (PDFContent)
    except:
        return ("Keine Daten auslesbar")
 
 
"""
Testcase
bild2.pdf und scan0033.pdf: keine Metadata, nicht durchsuchbar
neu0040-A2-b.pdf, GLS.pdf, ba014394: Metadata, durchsuchbar
"""

"""
files = ["Testfiles/bild2.pdf", "Testfiles/neu0040-A2-b.pdf", "Testfiles/GLS.pdf", "Testfiles/ba014394.pdf", "Testfiles/scan0033.pdf"]
for fileName in files:
    
    response = checkPDFSeachability(fileName)
    print (fileName + " ist durchsuchbar " + response)
    
    # fileName = 'Testfiles/KUG.pdf'    
    response = getPDFMetaData(fileName)
    print (fileName + "-----------------------------------------------------")
    print (response)
    
    response = getPDFContent(fileName)
    print (fileName + "-----------------------------------------------------")
    print (response)
    """
    