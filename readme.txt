HOW TO RUN
-----------

1. Place your resumes in the folder "Resumes" (the name should be exactly the same like this).
2. Run the file named as ResumeExtractor.py and it will create a dataframe with the names of the people with their educational qualifications.
3. One of the code segments inside the main file contains a snippet to output the qualifications in a text file.
4. For files in extension ".doc", the converter.py can be used to convert them into .docx. This can only be run for ubuntu(as of now) where it converts successfully.


## Notes for the developer ##

Things that should be taken care of.

1. Resumes with images.
2. Resumes with no educational section.



Further Improvements

1. Some functions may be combined as they may similar input like the return_headings and return_lines.

2. Classes can be used, where each object could store one resume, thus some class attributes exclusive to each object can hold some values such as the line number of keywords so that they are not calculated again and again. 

3. Does not do well for pdfs.
