from docx2python import docx2python
import re

text = docx2python('SK.docx').text
lines = [sentences for sentences in text.split("\n") if len(sentences)>0]


# Returns the educational qualifications from the starting index of educational section
def return_education_points(headingsDict):
    education_qualifications = []
    desired_index=None
    next_index = None
    
    for headings,index in headingsDict.items():
        next_index = index
        
        # Break the loop when we have both the educational section and the next column's index
        if desired_index is not None:
            break
        
        if re.match("education*",headings,re.I):
            desired_index = index
            continue
        
        
    # If an educational section exists
    if desired_index is not None:
        
        # If in case the educational section is the last section, print till end of doc, otherwise till next heading
        if next_index!=desired_index:
            return lines[desired_index+1:next_index]
        else:
            return lines[desired_index+1:len(lines)]

# Function to determine the headings in the resume
def return_headings(lines):
     headingsDict = {}   
     for lineNo in range(len(lines)):
         try:
             if re.match("--\\t*",lines[lineNo])==None and re.match("--\\t*",lines[lineNo+1]):
                 headingsDict[lines[lineNo].strip()] = lineNo
         except IndexError:
             break
     return headingsDict

# Formatting and refining the output
def format_points(education_points):
    if education_points is not None: return [points[3:] for points in education_points]

print(format_points(return_education_points(return_headings(lines))))



#%% This cell is just used to print stuff

# education_lines=return_education_index(lines)
# print(return_education_points(education_lines)[:3])    
    