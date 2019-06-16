#!/bin/python
#PDF Reader
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

# Iterate all the pages
 
# Using regex to filter only words and numbers
 
# Concatenate the words in each page
 
string_words = ''
for pageno in range(no_of_pages):
    pi = pdffile.getPage(pageno)
    page = pdffile.getPage(pageno)
    content = page.extractText()
    textonly = re.findall(r'[a-zA-Z0-9]+', content)
    for word in textonly:
        string_words = string_words + ' ' + word
 
# Convert the string of words to mp3 file 
print(string_words)
tts = gTTS(text=string_words, lang='en')
tts.save("listen_pdf.mp3")