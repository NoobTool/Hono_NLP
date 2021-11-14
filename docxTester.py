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





for paragraph in doc.paragraphs:
    
    for run in paragraph.runs:
        
        print(run.text)
        if len(headingsList)==2:
            pass
        
        if len(headingsList)==1 and run.text.strip()!='':
            headingsList.append(run.text)
            print(run.style.name)
            
        if re.match("educat*",run.text,re.I) or re.match("acade*",run.text,re.I):
            headingsList.append(run.text)
            print(run.style.name)
            
        break

#%%
print(headingsList)