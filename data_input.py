import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')

with open("EsEn_NER\calcs_dev.tsv", encoding='utf-8') as file:
    data = file.readlines()

    tweet = ""
    t = ""
    for line in data:
        line  = line.split("\t")        
        if line[0] != t:
            doc = nlp(tweet) 
            print(*[f'token: {ent.text}\tner: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')
            t = line[0]
            tweet = line[4]
        else:
            
            tweet += " " + line[4] + " "
    