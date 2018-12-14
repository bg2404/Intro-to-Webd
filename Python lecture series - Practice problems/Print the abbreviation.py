num_of_string = int(input("Enter the number of string(s)\n"))
names = [input().split() for x in range(num_of_string)]
abbreviations = ["".join([word[0] for word in name]) for name in names]
for abbreviation in abbreviations: print(abbreviation)