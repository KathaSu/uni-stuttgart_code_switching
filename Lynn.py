#import en_core_web_sm
import spacy
#nlp = en_core_web_sm.load()
nlp = spacy.load("en_core_web_sm")
nlp_es = spacy.load("es_core_news_sm")
doc = nlp("Angela Merkel lives in Berlin. And likes eating bananas. She hates Donald Trump.")
doc2 = nlp_es("Angela Merkel vive en Berlín. Y le gusta comer bananas. Ella odia a Donald Trump.")

for ent in doc.ents:
    print(ent.text, ent.label_,)

for ent in doc2.ents:
    print(ent.text, ent.label_)

for ent in doc2.ents:
    print(ent.text, ent.label_)


#git testing...