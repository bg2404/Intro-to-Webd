numbers = [int(x) for x in input().split()]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
for key, value in frequency.items():
    print(key,':',value)