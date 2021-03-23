import magic
import os
import logging
logging.basicConfig(format='%(asctime)s - %(message)s')

"""
Diese Funktion ermittelt den Dokumenttyp und prüft diesen auf Zulässigkeit. 
Zulässig sind:
- PDF
- JPEG
- PNG
- BNP (Bitmap)
"""
def checkFileType(fileName):
    logging.warning("checkFileType with " + fileName + " invoked")
    
    fileType = magic.from_file(fileName).upper()

    if 'PDF' in fileType:
        return ('PDF detected: Type supported')
    elif 'JPEG' in fileType:
        return ('JPG detected: Type supported')
    elif 'PNG' in fileType:
        return ('PNG detected: Type supported')
    elif 'BITMAP' in fileType:
        return ('BMP detected: Type supported')  
    else: 
        return ('Unsupported FileType')

# Diese Funktion ermittelt die Größe eines Dokument und prüft diese auf Zulässigkeit    
def checkFileSize(fileName):
    logging.warning("checkFileSize with " + fileName + " invoked")

    
    size = os.stat(fileName).st_size
    # print (size)
    if size >= 9000000: # 9MByte
        return ('false') # Datei größer als 9MB
    else:
        return ('true') # Datei kleiner als 9 MB

""" 
Testcase       
bild2.png:        PNG > 9MB
neu0040-A2-b.pdf: PDF < 9 MB
bild2.jpg:        JPEG < 9MB
bild2.png:        PNG > 9 MB
bild2.bmp         Bitmap > 9 MB
watermark.ps      Postscript datei < 9 MB
"""
"""
files = ["Testfiles/bild2.pdf", "Testfiles/neu0040-A2-b.pdf","Testfiles/bild2.jpg", "Testfiles/bild2.png", "Testfiles/bild2.bmp", "Testfiles/watermark.ps"]
for fileName in files:
    response = checkFileType(fileName)
    print (fileName + " " + response)

    response = checkFileSize(fileName)
    print (fileName + " " + response)
    """
    
