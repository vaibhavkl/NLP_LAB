##Name:- LOKHANDE VAIBHAV KISHOR
##ROLL NO. :- 37(UIT20M1039)
##ASSIGNMENT NO. 1
##Natural Language Processing With spaCy in Python

#IMPORTED SPACY LIBRARY FOR PROCESSING
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














# /bin/python3 /home/exam/NLP_lab/NLP_LAB/Assignment_NO_1.py




#  -----------------------TOKKENIZATION-------------------------

# NLP 0
# enables 4
# computers 12
# to 22
# understand 25
# natural 36
# language 44
# as 53
# humans 56
# do 63
# . 65
# Whether 66
# the 74
# language 78
# is 87
# spoken 90
# or 97
# written 100
# , 107
# natural 108
# language 116
# processing 125
# uses 136
# artificial 141
# intelligence 152
# to 165
# take 168
# real 173
# - 177
# world 178
# input 184
# , 189
# process 191
# it 199
# , 201
# and 202
# make 206
# sense 211
# of 217
# it 220
# in 223
# a 226
# way 228
# a 232
# computer 234
# can 243
# understand 247
# . 257




#  -----------------------STOP WPRDS -------------------------

# four
# about
# say
# may
# without
# he
# ten
# wherein
# itself
# an




#  -----------------------LEMMATIZATION -------------------------

#              enables : enable
#            computers : computer
#               humans : human
#              Whether : whether
#                   is : be
#               spoken : speak
#              written : write
#                 uses : use


#   -----------------------POS TAGGING -------------------------


# TOKEN: NLP
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: enables
# =====
# TAG: VBZ        POS: VERB
# EXPLANATION: verb, 3rd person singular present

# TOKEN: computers
# =====
# TAG: NNS        POS: NOUN
# EXPLANATION: noun, plural

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: understand
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: natural
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: language
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: as
# =====
# TAG: IN         POS: SCONJ
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: humans
# =====
# TAG: NNS        POS: NOUN
# EXPLANATION: noun, plural

# TOKEN: do
# =====
# TAG: VBP        POS: VERB
# EXPLANATION: verb, non-3rd person singular present

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: Whether
# =====
# TAG: IN         POS: SCONJ
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: language
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: spoken
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: or
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: written
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: natural
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: language
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: processing
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: uses
# =====
# TAG: VBZ        POS: VERB
# EXPLANATION: verb, 3rd person singular present

# TOKEN: artificial
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: intelligence
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: take
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: real
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: -
# =====
# TAG: HYPH       POS: PUNCT
# EXPLANATION: punctuation mark, hyphen

# TOKEN: world
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: input
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: process
# =====
# TAG: VBP        POS: VERB
# EXPLANATION: verb, non-3rd person singular present

# TOKEN: it
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: and
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: make
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: sense
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: of
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: it
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: in
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: way
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: computer
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: can
# =====
# TAG: MD         POS: AUX
# EXPLANATION: verb, modal auxiliary

# TOKEN: understand
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer