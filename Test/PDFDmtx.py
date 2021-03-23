from pylibdmtx.pylibdmtx import decode
from cv2 import cv2
import uuid
import pdf2image

         
fileID = str(uuid.uuid4())
print (fileID + '0001-1.png')
           
image = pdf2image.convert_from_path('Testfiles/wba.pdf', dpi=200, output_folder='/home/hthierbach', first_page=1, last_page=1, output_file=fileID, fmt='png')                
image = cv2.imread('/home/hthierbach/' + fileID +'0001-1.png',0)


height, width = image.shape[:2]
# print (decode((image.tobytes(), width, height)))
print (decode(image))

"""
https://pypi.org/project/pylibdmtx/

Ausgabe:
b0c76255-99a1-4ff8-ba75-fde8a81ae50c0001-1.png
[Decoded(data=b'I#042                                                     ANTRAG      90011UB', rect=Rect(left=791, top=986, width=198, height=197))]

Note: Läuft sehr lange!!!
"""