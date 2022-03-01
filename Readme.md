## PDF Combine script

This is a basic script that combines PDF files using PyPDF2.
I made this as a general use thing for my own stuff but I figured I'd put it up here anyway.

# Doing the thing
Simply run the script with `python combinepdf.py` or `python3 combinepdf.py` (depending on your python install)

The program will prompt you to select files.
You can select multiple pdf files at once, or you can select them individually if you have a specific order in mind
Once you've selected your file(s), it will prompt you to select more (if you want a particular order),
    - To combine the files you're already selected just hit 'cancel' and it will run.

It will then prompt you to enter a filename in the command line, if you do nothing, default output is 'out.pdf'

# Requirements

    - Python 3.x
    - tkinter (should come with python)
    - PyPDF2

Install with `pip install -r requirements.txt`