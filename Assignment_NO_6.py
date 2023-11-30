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
vaibhav is Python Developer
He is good looking
He is very Famous
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

'''
TTOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'vaibhav'
token.dep_ = 'dep'

TOKEN: vaibhav
=====
token.tag_ = 'VB'
token.head.text = 'vaibhav'
token.dep_ = 'ROOT'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'vaibhav'
token.dep_ = 'auxpass'

TOKEN: Python
=====
token.tag_ = 'NNP'
token.head.text = 'Developer'
token.dep_ = 'compound'

TOKEN: Developer
=====
token.tag_ = 'NNP'
token.head.text = 'He'
token.dep_ = 'compound'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Developer'
token.dep_ = 'dep'

TOKEN: He
=====
token.tag_ = 'PRP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: good
=====
token.tag_ = 'JJ'
token.head.text = 'is'
token.dep_ = 'acomp'

TOKEN: looking
=====
token.tag_ = 'VBG'
token.head.text = 'is'
token.dep_ = 'xcomp'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'looking'
token.dep_ = 'dep'

TOKEN: He
=====
token.tag_ = 'PRP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: very
=====
token.tag_ = 'RB'
token.head.text = 'Famous'
token.dep_ = 'advmod'

TOKEN: Famous
=====
token.tag_ = 'JJ'
token.head.text = 'is'
token.dep_ = 'acomp'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Famous'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...
'''

127.0.0.1 - - [28/Nov/2023 14:39:36] "GET / HTTP/1.1" 200 10912
127.0.0.1 - - [28/Nov/2023 14:39:36] "GET /favicon.ico HTTP/1.1" 200 10912

"""
