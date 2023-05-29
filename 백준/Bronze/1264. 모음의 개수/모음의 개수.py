mo = ['a','e','o','u','i','A','E','O','U','I']

while True:
    count = 0
    N = input()
    if N == '#':
        break
    for s in N:
        if s in mo:
            count += 1
    print(count)