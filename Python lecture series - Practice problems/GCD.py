def gcd(a, b):
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
        return gcd(min(a,b), max(a,b) % min(a,b))

print(gcd(int(input()),int(input())))