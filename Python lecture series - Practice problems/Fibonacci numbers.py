n = int(input())

fibonacci = [0, 1]

if n > 2:
    for i in range(3, n+1):
        fibonacci.append(fibonacci[i-3]+fibonacci[i-2])
for i in range(n):
    print(fibonacci[i])