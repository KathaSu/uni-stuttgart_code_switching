import sys

F = open(sys.argv[1])
tweets = 0
t = ""
for line in F:
    line = line.split("\t")
    if line[0] != t:
        tweets += 1
        t = line[0]

print(tweets)
