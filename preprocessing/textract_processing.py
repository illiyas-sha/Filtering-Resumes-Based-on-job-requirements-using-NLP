import textract             #package provides a single interface for extracting content from any type of file
import re

def get_content_as_string(filename):
    text = textract.process(filename)                       #  To obtain text from a document
    lower_case_string = str(text.decode('utf-8')).lower()   # converts text string to utf-8 and returns lowercase

    return lower_case_string
