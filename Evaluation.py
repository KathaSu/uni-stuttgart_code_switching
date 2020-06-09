

output = open('output.txt', encoding='utf-8')
dev = open('EsEn_NER\calcs_dev.tsv', encoding='utf-8')

outputdata = output.readlines()
devdata = dev.readlines()

for line_output, line_dev in zip(outputdata, devdata):
    line_output = line_output.split("\t")
    line_dev = line_dev.split("\t")    
    if line_output[] == line_dev[0]:
        print(line_output)