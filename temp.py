from docx2python import docx2python
import re

text = docx2python('SK.docx').text
lines = [sentences for sentences in text.split("\n") if len(sentences)>0]


# Returns the index where educational information starts
def return_education_index(lines):
    index=0
    for x in lines:
        if re.match("EDUCATION*",x,re.I):
            return index
        index+=1

    return None

# Returns the educational qualifications from the starting index of educational section
def return_education_points(index):
    education_qualifications = []
    for line in range(index,len(lines)):
        if re.match("--\\t*",lines[line]):
            education_qualifications.append(lines[line])
            
    return education_qualifications


# Function to determine the headings in the resume
def return_headings(lines):
    print(lines)
    
return_headings(lines)




#%% This cell is just used to print stuff

# education_lines=return_education_index(lines)
# print(return_education_points(education_lines)[:3])    
    