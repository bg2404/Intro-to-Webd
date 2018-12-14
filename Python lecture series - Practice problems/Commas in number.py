# Assuming number of input integers to be 5
def addCommas(a):
    a = "".join([l + ','*(n%3 == 2) for n, l in enumerate(list(a[::-1]))])[::-1]
    if(a[0] == ','):
        a = "".join(list(a)[1:])
    return a

numbers = [addCommas(number) for number in input().split()]
for number in numbers: print(number)