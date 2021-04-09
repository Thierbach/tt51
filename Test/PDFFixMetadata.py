import ghostscript
import logging
logging.basicConfig(format='%(asctime)s %(message)s')


def fixPDFMetaData(infile, outfile):   
    logging.warning('Function fixMetaData invoked ...') 
    args = [
        "ps2pdf", # actual value doesn't matter
        "-dNOPAUSE", "-dBATCH", "-dSAFER",
        "-sDEVICE=pdfwrite",
        "-sOutputFile=" + outfile,
        "-c", "3000000 setvmthreshold",
        "-f",  infile
        ]
    
    args = [a.encode('utf-8') for a in args]
    
    ghostscript.Ghostscript(*args)

    return('Done')


logging.warning(fixPDFMetaData('Testfiles/ferien10.pdf', 'Testfiles/corrected_ferien10.pdf'))