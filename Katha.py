import stanza

#stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
doc = nlp("Why	doesn't	Louis Vuitton make men's watches 😔	")
print(*[f'token: {token.text}\tner: {token.ner}' for sent in doc.sentences for token in sent.tokens], sep='\n')


