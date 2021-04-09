"""
sudo apt-get install clamav clamav-freshclam 
sudo apt-get install clamav-daemon 
sudo dpkg-reconfigure clamav-base 
"""

import re
import logging
import pyclamd
import os
logging.basicConfig(format='%(asctime)s %(message)s')

"""
Diese Funktion liest einen Text ein und escaped alle potentiellen gefährlichen Zeichen
"""
def documentEscaper(fileName):
    prefix = 'Testfiles/'
    logging.warning('documentEscaper invoked with File: ' + fileName)
    
    # Datei öffnen 
    suspiciousFile = open(prefix + fileName, 'rt')

    # DateiInhalt lesen
    suspiciousData = (suspiciousFile.read())
       
    # zulässige Zeichen sind [a-Z0-9äÄüÜöÖß.-,!"`''@], alle anderen werden escaped
    escapedData =  (re.sub(r'([\;\\\+\*\?\[\^\]\$\&\{\}\[\]\!\<\>\\^\°\=\#\(\)\:\§\"\|])', r'\\\1', suspiciousData))
    logging.warning(escapedData)
    
    # Datei schreiben
    escapedFile = open(prefix + 'escaped' + fileName, 'wt')
    escapedFile.write(escapedData)
    
    # Files schließen
    suspiciousFile.close()
    escapedFile.close()
    
    return()
    
    
    
def documentVirusScan(fileName):
    prefix = '/Testfiles/'
    logging.warning('documentVirusScan invoked with File: ' + fileName)
    logging.warning('Working on Path: ' + os.getcwd())
    path = os.getcwd()
        

    AntiVirusInstance = pyclamd.ClamdAgnostic()
    # prüfe die Deamon Instanz
    try:
        #AntiVirusInstance = pyclamd.ClamdUnixSocket() # kann auch via Socket aufgerufen werden, wenn konfiguriert
        
        # prüfen, ob der AV-Server Prozess erreichbar ist
        StatusAVDaemon = AntiVirusInstance.ping()
        if (StatusAVDaemon):
            logging.warning('Deamon is running')
        else:
            logging.warning('No Deamon found')
    except:
        return ('Server not runnung ...')
    
    # Virus Signature Datei neu laden
    # logging.warning(AntiVirusInstance.reload())
    
    # Datei scannen
    logging.warning(AntiVirusInstance.scan_file(path + prefix + fileName))
    
    # Ergebnis auswerten
    if (AntiVirusInstance.scan_file(path + prefix + fileName)):
        result = 'Virus Infection detected'
    else:
        result = 'No Virus detected'
        
    return (result)
    
      
    
    
    
# print(documentEscaper('EICAR.txt'))

print(documentVirusScan('EICAR.txt'))
# print(documentVirusScan('escapedEICAR.txt'))

