# pdfmerge
CLI-ready Python tool to merge two or more pdf files into one (based on pyPdf).

#### Requirements
Python 2.7
pyPdf library

#### Syntax
python pdfmerge.py <filebase>

#### Use Case
Save two or more numerically ordered pdf files with the same base file name (i.e. image0, image1, image2).  Run 'python pdfmerge.py image' to concatenate the input image files into one output file called "testout.pdf".

#### Notes
I wrote this python script quickly one afternoon (late 2013) because I needed to send a multi-page document with signatures and/or annotations.  It was a trivial exercise, used intermittently, and never updated.  Since then, many choices for document sharing and capture have emerged.  Why post this now?  A company that I am advising is building a platform for the incentivization of open source projects.  This repo is perfect the alpha test. It's not critical and has plenty of tiny little things that can be fixed.
