# Assignment No 3
# Name - Vaibhav Lokhande
# Batch - B2
# Roll No - 37
# Assignment Title : Implement Named Entity Recognition(NER) on textual data using SpaCy library for English language.


import spacy


# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Extract named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

if __name__ == "__main__":
    # Example text
    text = "John   lives in New York and Loves to eat mangoes"

    # Perform Named Entity Recognition
    named_entities = perform_ner(text)

    # Print the results
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")

# OUTPUT -
''' 
Named Entities:
John - PERSON
New York - GPE 
'''
