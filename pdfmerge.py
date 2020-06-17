# PDF file concatenator
# - from multiple files with the same base name, make one PDF file
# - expects input file base, accepts output file name 
# - subprocess: http://stackoverflow.com/questions/89228/calling-an-external-command-in-python?rq=1

import sys, subprocess
from pyPdf import PdfFileWriter, PdfFileReader

# test base name of the input files, how many files exist?
if len(sys.argv) > 1:
    ifilebase = sys.argv[1]
else:
    print 'pdfmerge requires an input file base name'
    sys.exit()

# test number of files
inputfilestest = 'ls '+ifilebase+'*.pdf'
p = subprocess.Popen(inputfilestest, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
if err:
    print err
    sys.exit()
else:
    filenames = out.split('\n')
    if not filenames[len(filenames)-1]:
        filenames.pop()
    numfiles = len(filenames)
    print 'merging', numfiles, 'files with base', ifilebase

# open a writer file
o = PdfFileWriter()

# open each input file and add to the writer file
for i in range(numfiles):
    ifile = PdfFileReader(file(filenames[i], "rb"))
    o.addPage(ifile.getPage(0))

os = file("testout.pdf", "wb")
o.write(os)
os.close()
