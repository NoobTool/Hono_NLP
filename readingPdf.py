import pdfplumber
import re
import temp as tp

with pdfplumber.open(r"./Resumes/DR.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    
lines = text.split("\n")


# Function to determine the headings in the resume
def return_headings(lines):
     headingsDict = {}   
     for lineNo in range(len(lines)):
         try:
             if re.match('\uf0b7+',lines[lineNo]) is None and re.match('\uf0b7+',lines[lineNo+1]) is not None:
                 headingsDict[lines[lineNo].strip()] = lineNo
         except IndexError:
             break
     print("Headings are:- ",headingsDict)
     return headingsDict
 
    
print(tp.format_points(tp.return_education_points(lines, return_headings(lines), None),'\uf0b7'))