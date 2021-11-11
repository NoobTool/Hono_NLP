import os
from pathlib import Path

location_of_resumes = os.path.join(Path.home(),"Downloads","res2")

def save_as_docx():
    os.popen("cd "+location_of_resumes+"; lowriter --convert-to docx *.doc")
    
    
save_as_docx()
    