import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import models

text2 = open('vaibhav.txt', encoding ='utf-8')
 
tokens2 =[]
for line in text2.read().split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)
g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("\n Bag of Words : ", g_bow)
print("\n")
print("--------------------------------------------------------------------------------------")

print("--------------------------------------TFIDF VECTOR------------------------------------")





##TFIDF
text = [ "NLP enables computers to understand natural language as humans do."
    "Whether the language is spoken or written,"
    "natural language processing uses artificial intelligence to take real-world input, process it,"
    "and make sense of it in a way a computer can understand."
]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("\n TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])


#output
'''The dictionary has: 34 tokens

{'as': 0, 'computers': 1, 'do': 2, 'enables': 3, 'humans': 4, 'language': 5, 'natural': 6, 'nlp': 7, 'to': 8, 'understand': 9, 'and': 10, 'artificial': 11, 'can': 12, 'computer': 13, 'in': 14, 'input': 15, 'intelligence': 16, 'is': 17, 'it': 18, 'make': 19, 'of': 20, 'or': 21, 'process': 22, 'processing': 23, 'real': 24, 'sense': 25, 'spoken': 26, 'take': 27, 'the': 28, 'uses': 29, 'way': 30, 'whether': 31, 'world': 32, 'written': 33}

 Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)], [(5, 2), (6, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 2), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1), (29, 1), (30, 1), (31, 1), (32, 1), (33, 1)], []]


--------------------------------------------------------------------------------------
--------------------------------------TFIDF VECTOR------------------------------------
Dictionary : 
[['and', 1], ['artificial', 1], ['as', 1], ['can', 1], ['computer', 1], ['computers', 1], ['do', 1], ['enables', 1], ['humans', 1], ['in', 1], ['input', 1], ['intelligence', 1], ['is', 1], ['it', 2], ['language', 3], ['make', 1], ['natural', 2], ['nlp', 1], ['of', 1], ['or', 1], ['process', 1], ['processing', 1], ['real', 1], ['sense', 1], ['spoken', 1], ['take', 1], ['the', 1], ['to', 2], ['understand', 2], ['uses', 1], ['way', 1], ['whether', 1], ['world', 1], ['written', 1]]

 TF-IDF Vector:
[['and', 0.14], ['artificial', 0.14], ['as', 0.14], ['can', 0.14], ['computer', 0.14], ['computers', 0.14], ['do', 0.14], ['enables', 0.14], ['humans', 0.14], ['in', 0.14], ['input', 0.14], ['intelligence', 0.14], ['is', 0.14], ['it', 0.27], ['language', 0.41], ['make', 0.14], ['natural', 0.27], ['nlp', 0.14], ['of', 0.14], ['or', 0.14], ['process', 0.14], ['processing', 0.14], ['real', 0.14], ['sense', 0.14], ['spoken', 0.14], ['take', 0.14], ['the', 0.14], ['to', 0.27], ['understand', 0.27], ['uses', 0.14], ['way', 0.14], ['whether', 0.14], ['world', 0.14], ['written', 0.14]]
Colab paid products - Cancel contracts here'''
