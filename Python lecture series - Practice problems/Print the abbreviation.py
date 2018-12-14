# Since there is no input for number of inputs I'm assuming there will be 4 input Stirngs
names = [input().split() for x in range(4)]
abbreviations = ["".join([word[0] for word in name]) for name in names]
for abbreviation in abbreviations: print(abbreviation)