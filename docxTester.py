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
    lines = [sentences for sentences in text.split("\n") if len(sentences)>0]

    return lines,doc,document


lines,doc,document = init_docx("Anuj Kumar")

print(lines)