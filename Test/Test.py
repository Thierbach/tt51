# -*- coding: utf-8 -*-
from pikepdf import Pdf
import xml.etree.ElementTree as ET



with Pdf.open("Testfiles/KUG.pdf") as pdf:
    xmp = pdf.Root.Metadata.read_bytes()    # xmp-Konten wird gelesen
    type(xmp)


namespaces = {"""xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.4-c005 78.150055, 2013/08/07-22:58:47" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" """}
root = ET.fromstring(xmp)
print (root.findall("*creator"))
