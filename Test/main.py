import os
from FileType import checkFileType, checkFileSize
from PDFType import checkPDFType
from PDFData import checkPDFSeachability, getPDFMetaData, getPDFContent

def worker(fileName):
    print (checkFileType(fileName))
    print (checkFileSize(fileName))

    print (checkPDFType(fileName))
    
    print (checkPDFSeachability(fileName))
    print (getPDFMetaData(fileName))
    print (getPDFContent(fileName))







"""
def worker():
    os.system('python3 FileType.py')
    os.system('python3 PDFType.py')
    os.system('python3 PDFData.py')
    # os.system('python3 PDFQRData.py')
    return ('worker startet')
    
    """


