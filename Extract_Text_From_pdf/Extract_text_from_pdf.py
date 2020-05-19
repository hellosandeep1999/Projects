# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:40:02 2020

@author: user
"""

"""
Extract text from PDF In python for NLP

"""

#step 1 - !pip install PyPDF2


#Now import the PyPDF2
import PyPDF2 as pdf


#file
file = open('NLP.pdf','rb')   #open our pdf for extracting the data




#pdf_reader
pdf_reader = pdf.PdfFileReader(file)
image = open('cafe.PNG','rb')



pdf_reader.getIsEncrypted()  #FAlse

pdf_reader.getNumPages()  #it will return number of pages in pdf


page1 = pdf_reader.getPage(0)
page1.extractText()


page2 = pdf_reader.getPage(1)
page2.extractText()


#Append Write or Merge PDf

pdf_writer = pdf.PdfFileWriter()


pdf_writer.addPage(page1)
pdf_writer.addPage(page2)


output = open('Pages.pdf','wb')    
pdf_writer.write(output)
output.close()



