# SEP
Project: Text Redaction

In this project, we created a system which detects "sensitive" items in the text. Once identified, the system will redact these sensitive items such as names, dates, addresses (city, state and country). After redacting the sensitive items, the program will save redacted file as a new file with the .txt extension in the current folder. We are using SpaCy module from Natural Language Processing with python.

* [x] Testing::

We can test the redactor project that we submitted by adding different person names, dates and addresses in the text file data.txt. 
After that by running python3 seppro.py, it will generate a redacted text file in the same directory with the redacted data.
We can verify the results by comparing the generated file with the input file. All the redacted fields will be replaced with [REDACTED].
