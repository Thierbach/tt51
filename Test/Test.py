# -*- coding: utf-8 -*-
from pikepdf import Pdf
import textract
from S3_Connector import S3_putObject, S3_getObject, S3_authorize


def my_function():
    print ("Hello World!")
        
my_function()


new_pdf = Pdf.new()
with Pdf.open('/home/hthierbach/neu0040-A2-b.pdf') as pdf:
    pdf.save('/home/hthierbach/output.tiff')
    meta = pdf.open_metadata()
    pdf_format = meta.pdfa_status
    if pdf_format == "":
        print ('PDF is not compliant with PDF/A standard')
    else:
        print ('PDF is ' + pdf_format)


xmp = pdf.Root.Metadata.read_bytes()
type(xmp)
print (xmp.decode())

"""

# print (pdf.docinfo)

text = textract.process('/home/hthierbach/ba014394.pdf', method='pdfminer')
u = text.decode('utf8')
print (u)

print ("Calling S3 Upload ...")
S3_putObject()

print ("Calling S3 Download ...")
S3_getObject()

"""