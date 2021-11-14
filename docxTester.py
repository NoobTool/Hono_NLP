from docx2python import docx2python
import re
from docx import Document
import os
import pdfplumber
import pandas as pd


def init_docx(fileName):
    file_path = 'Resumes/{}.docx'.format(fileName)
    document = docx2python(file_path)
    doc2 = docx2python(file_path,html=True)
    doc = Document(file_path)
    text = doc2.text
    lines = [sentences.strip() for sentences in text.split("\n") if len(sentences.strip())>0]

    return lines,doc,document


lines,doc,document = init_docx("Nikita Garg")

headingsList = []

def return_lines_using_wordCount(lines):
    
    lineNumber = [lineNo for lineNo in range(len(lines)) if check_for_keywords(lines[lineNo])][0]
    temp = lineNumber+1
    
    try:    
        while(len(lines[temp].split(" "))>=3 and re.match("[0-9]+/.*")):
            temp+=1
    except IndexError:
        pass
    return retLines(lines,lineNumber+1,temp+1)

#%%
print(headingsList)