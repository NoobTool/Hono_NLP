from docx2python import docx2python
import re
from docx import Document
import os
import pdfplumber
import pandas as pd


def init_docx(fileName):
    file_path = 'Resumes/{}.docx'.format(fileName)
    document = docx2python(file_path)
    # doc2 = docx2python(file_path,html=True)
    doc = Document(file_path)
    text = document.text
    lines = [sentences for sentences in text.split("\n") if len(sentences)>0]

    return lines,doc,document


def init_pdf(fileName):
    with pdfplumber.open(r"./Resumes/{}.pdf".format(fileName)) as pdf:
        text = pdf.pages[0].extract_text()
        lines = text.split("\n")

    return lines,doc


# Returns the educational qualifications from the starting index of educational section
def return_education_points(lines, headingsDict, bold_text):
    
    desired_index=None
    next_index = None
    
     
    for headings,index in headingsDict.items():
        next_index = index
        
        # Break the loop when we have both the educational section and the next column's index
        if desired_index is not None:
            break
        
        if re.match("education*",headings,re.I) or re.match("academic*",headings,re.I) or re.search("qualific*",headings,re.I) is not None:
            desired_index = index
            continue
    
    if desired_index is None:
        for headings,index in bold_text.items():
            next_index = index
            
            # Break the loop when we have both the educational section and the next column's index
            if desired_index is not None:
                break
            
            if re.match("education*",headings,re.I) or re.match("academic*",headings,re.I) or re.search("qualific*",headings,re.I) is not None:
                desired_index = index
                continue
        
        
    # If an educational section exists
    if desired_index is not None:
        
        # If in case the educational section is the last section, print till end of doc, otherwise till next heading
        if next_index!=desired_index:
            return lines[desired_index+1:next_index]
        else:
            return lines[desired_index+1:len(lines)]
        
    else:
        return check_each_line(lines,document)

# Function to determine the headings in the resume
def return_headings(lines):
     headingsDict = {}   
     for lineNo in range(len(lines)):
         try:
             if (re.match("--\\t*",lines[lineNo])==None and re.match("--\\t*",lines[lineNo+1])) or\
             (re.match('\uf0b7+',lines[lineNo]) is None and re.match('\uf0b7+',lines[lineNo+1]) is not None):
                 headingsDict[lines[lineNo].strip()] = lineNo
         except IndexError:
             break
     print("Headings are:- ",headingsDict)
     return headingsDict


# Check for bold text
def return_bold_text(doc,lines):
    
    # Dictionary for bold text
    bold_text = {}
    
    # Dictionary for bold and capital text
    bold_text_priority = {}
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            
            # Headings in resumes do not take more than 7 words, doesn't contain special chars and numbers
            if (run.bold or re.sub("[,:]","",run.text).isupper()) and len(run.text.split(" "))<7 and re.search("[0-9]",paragraph.text) is None:
                # Lines with all words in capital have more chances to be in headings
                try:
                    if run.text.isupper():
                        bold_text_priority[run.text]=lines.index(run.text)
                    else:
                        bold_text[run.text]=lines.index(run.text)
                except ValueError:
                    pass      
    print(bold_text_priority)
    return bold_text_priority


# Check each line for educational qualifications
def check_each_line(lines,document):
    lines = document.text.splitlines(True)
    lines2 = [line for line in lines if len(line.split(" "))<7]
    education_lines = [line for line in lines2 if check_for_keywords(line)]
    # education_lines = [line for line in lines2 if re.match("educat*",line,re.I)]
    try:
        starting_index = lines.index(education_lines[0])+1
        ending_index = len(lines)
        
        for x in range(starting_index,len(lines)):
            try:
                if lines[x+1]=='\n' and lines[x+2]=='\n':
                    ending_index = x+2
                    
            except IndexError:
                pass
                
        education_lines = lines[starting_index:ending_index-1]
        education_lines = list(filter(('\n').__ne__,education_lines))
        education_lines = [line.replace('\n','') for line in education_lines]
        
        return education_lines

    except IndexError:
        return ["404"]

def check_for_keywords(headings):
    if re.match("education*",headings,re.I) or re.match("academic*",headings,re.I) or re.search("qualific*",headings,re.I) is not None:
        return True
    else: False

# Formatting and refining the output
def format_points(education_points,*charReplacements):
    
    for replacement in charReplacements:
        education_points = [points.replace(replacement,"") for points in education_points]
        
    # education_points = [points.replace("--\\t","") for points in education_points]
    # education_points = [points.replace("\t","") for points in education_points]
    return education_points
    

#%% This cell is just used to print stuff
# print("\n\n",format_points(return_education_points(return_headings(lines),return_bold_text())))

if __name__ == '__main__':
    
    # Using dataframes to carry the content of all resumes
    df = pd.DataFrame(columns=['Name','Qualifications'])
    
    cwd = os.getcwd()
    getCurrentFileNames = os.listdir(cwd+"/Resumes/")
    
    for files in getCurrentFileNames:
        fileName = files.split(".")
        try:
            if fileName[1]=='docx':
                lines,doc,document = init_docx(fileName[0])
                content_to_be_written = format_points(return_education_points(lines,return_headings(lines),return_bold_text(doc,lines)),"--\\t","\t")
            else:
                lines,doc = init_pdf(fileName[0])
                content_to_be_written = format_points(return_education_points(lines,return_headings(lines),return_bold_text(doc,lines)),"\uf0b7")
                
            df.loc[len(df.index)] = [fileName[0],content_to_be_written ]
                

            # The code to write the output in a text file
            with open(cwd+"/Output/"+fileName[0]+".txt","w") as f:
                for content in content_to_be_written:
                    f.write(content+"\n")
        
        except FileNotFoundError:
            print("The docx version of this file does't exist.")
            
            
#%% Checking for individual resumes (only for testing purposes)

anujBhai = df.loc[df['Name']=='Anuj Kumar','Qualifications']

            
#%% Failure count

series_of_failures = df['Qualifications'].apply(lambda x: 1 if '404' in x else 0).tolist()
print(series_of_failures.count(0)*100/len(series_of_failures))



