with open("EsEn_NER\calcs_dev.tsv", encoding='utf-8') as file:
    data = file.readlines()

    tweet = ""
    t = ""
    for line in data:
        line  = line.split("\t")        
        if line[0] != t:
            t = line[0]
            tweet = line[4]
        else:
            tweet += " " + line[4] + " "
    print(tweet)
    