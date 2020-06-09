import stanza


class StanzaNER():

    def __init__(self, inputfile, outputfile):
        self.input = inputfile
        self.output = outputfile
        self.NERprocessing(self.input, self.output)

    def NERprocessing(self, inputfile, outputfile):
        nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
        inputfile = open(self.input, encoding='utf-8')
        outputfile = open(self.output, 'w', encoding='utf-8')
        data = inputfile.readlines()
        tweet = ""
        t = ""
        for line in data:
            line = line.split("\t")
            if line[0] != t:
                doc = nlp(tweet)
                print(tweet)
                for sent in doc.sentences:
                    for token in sent.tokens:
                        outputfile.write(t + '\t' + token.text + '\t' + token.ner + '\n')
                t = line[0]
                tweet = line[4]
            else:
                tweet += " " + line[4] + " "


StanzaNER("EsEn_NER\calcs_dev.tsv", "output.txt")

