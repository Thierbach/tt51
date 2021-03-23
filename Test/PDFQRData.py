from pyzbar.pyzbar import decode
from cv2 import cv2
import uuid
import pdf2image

         
fileID = str(uuid.uuid4())
print (fileID + '0001-1.png')
           
image = pdf2image.convert_from_path('Testfiles/QR-Codes.pdf', dpi=200, output_folder='/home/hthierbach', first_page=1, last_page=1, output_file=fileID, fmt='png')                
image = cv2.imread('/home/hthierbach/' + fileID +'0001-1.png',0)

# QR-Code
# print (image)
detectedBarCode = decode(image)
# print (detectedBarCode)

for barcode in detectedBarCode:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    
    
# https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/




