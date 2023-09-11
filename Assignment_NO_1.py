##Name:- LOKHANDE VAIBHAV KISHOR
##ROLL NO. :- 37(UIT20M1039)
##ASSIGNMENT NO. 1
##Natural Language Processing With spaCy in Python


import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "NLP enables computers to understand natural language as humans do."
    "Whether the language is spoken or written,"
    "natural language processing uses artificial intelligence to take real-world input, process it,"
    "and make sense of it in a way a computer can understand."
)

print("\n\n\n\n -----------------------TOKKENIZATION-------------------------\n")
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

print("\n\n\n\n -----------------------STOP WPRDS -------------------------\n")

##STOP WORDS
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

print("\n\n\n\n -----------------------LEMMATIZATION -------------------------\n")


##LEMMATIZATION
conference_help_doc = nlp(about_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


print("\n\n  -----------------------POS TAGGING -------------------------\n")

## POS TAGGING
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )