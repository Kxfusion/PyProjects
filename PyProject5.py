from urllib import request
from urllib.parse import quote

def read_text():
    quotes = open(b"C:\Users\kxfus\Documents\ProfText.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)
    

def check_profanity(text):
    parsedText = quote(text)
    connection = request.urlopen("http://www.wdylike.appspot.com/?q="+parsedText)
    output = connection.read()
    connection.close()
    if b"true" in output:
        print("Profanity Alert!!")
    elif b"false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    
read_text()
