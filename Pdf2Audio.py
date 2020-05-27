#!/bin/python
import PyPDF2
import os
from gtts import gTTS
import re

file_path = input("Enter full path to PDF to read: ")

if(os.path.exists(file_path)):
    pass
else:
    print("File does not exist!")
    
f = open(file_path, 'rb')


# get number of pages in pdf
pdffile = PyPDF2.PdfFileReader(f)
no_of_pages = pdffile.getNumPages()


# iterate through the pages
# use regex to filter only words and numbers
# concatenate the words in each page
string_words = ''
for pageno in range(no_of_pages):
    pi = pdffile.getPage(pageno)
    page = pdffile.getPage(pageno)
    content = page.extractText()
    textonly = re.findall(r'[a-zA-Z0-9]+', content)
    for word in textonly:
        string_words = string_words + ' ' + word
 

# convert string of words to mp3 file 
print(string_words)
tts = gTTS(text=string_words, lang='en')
tts.save("listen_pdf.mp3")
