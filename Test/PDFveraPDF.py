"""
https://docs.verapdf.org/install/
"""

import subprocess

# Diese Funktion liefert true zurück, wenn das PDF dem Profile A2-b entspricht
def PDFFormatValidation(fileName):
    path = "/home/hthierbach/verapdf/verapdf -f 2b "
    validationResult = subprocess.call(path + fileName, shell=True)
    return validationResult


files = ('test-A2-b.pdf', 'bild2.pdf')
for fileName in files:
    print (PDFFormatValidation('Testfiles/' + fileName))

