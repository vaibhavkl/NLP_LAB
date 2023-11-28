"""
Assignment No 6
Name - Vaibhav Lokhande
Batch - B2
Roll No - 37
Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

"""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
I am a Spark Developer 
Working in Multi National Compony
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

# OUTPUT -

"""

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'am'
token.dep_ = 'dep'

TOKEN: I
=====
token.tag_ = 'PRP'
token.head.text = 'am'
token.dep_ = 'nsubj'

TOKEN: am
=====
token.tag_ = 'VBP'
token.head.text = 'am'
token.dep_ = 'ROOT'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'Developer'
token.dep_ = 'det'

TOKEN: Spark
=====
token.tag_ = 'NNP'
token.head.text = 'Developer'
token.dep_ = 'compound'

TOKEN: Developer
=====
token.tag_ = 'NNP'
token.head.text = 'Working'
token.dep_ = 'compound'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Developer'
token.dep_ = 'dep'

TOKEN: Working
=====
token.tag_ = 'NNP'
token.head.text = 'am'
token.dep_ = 'attr'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'Working'
token.dep_ = 'prep'

TOKEN: Multi
=====
token.tag_ = 'NNP'
token.head.text = 'Compony'
token.dep_ = 'compound'

TOKEN: National
=====
token.tag_ = 'NNP'
token.head.text = 'Compony'
token.dep_ = 'compound'

TOKEN: Compony
=====
token.tag_ = 'NNP'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Compony'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...

127.0.0.1 - - [28/Nov/2023 14:39:36] "GET / HTTP/1.1" 200 10912
127.0.0.1 - - [28/Nov/2023 14:39:36] "GET /favicon.ico HTTP/1.1" 200 10912

"""