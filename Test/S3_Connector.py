import os
from minio import Minio
from minio.error import ResponseError
from boto3 import client

usr = 'minio'
pwd = 'miniostorage'


def S3_authorize():
    global client
    client = Minio(
        'localhost:9000',
        access_key=usr,
        secret_key=pwd,
        secure=False
    )
    

# Syntax Quellbucketname, zu holende S3-Datei, Zieldatei mit Pfad
def S3_getObject(bucketName, fileName, targetName):
    S3_authorize()
    try:
        result = client.get_object(bucketName, fileName)
        with open(targetName, 'wb') as file_data:
            for d in result.stream(32*1024):
                file_data.write(d)
        return ('Datei von S3 holen: success')
    except ResponseError as err:
        print(err)
        return ('error')
        

# Syntax Zielbucket, zu schreibende S3-Datei, Quelldatei mit Pfad    
def S3_putObject(bucketName, fileName, sourceName):
    S3_authorize()   
    try:
        result = client.fput_object(
            bucketName, fileName, sourceName
            )
        return ('Datei nach S3 schreiben: success')
    except ResponseError as err:
        print(err)
        return ('error')
    


# Testcase
result = S3_getObject('keep-in', 'bild.pdf', '/home/hthierbach/my-testfile.pdf')
print (result)

result = S3_putObject('keep-out', 'my-testfile.pdf', '/home/hthierbach/my-testfile.pdf')
print (result)





