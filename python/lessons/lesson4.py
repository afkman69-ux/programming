a = int(input())

if a > 50000:
    print(a - (a * 0.20))
elif 20000 < a < 50000:
    print(a - (a * 0.10))
else:
    print(a)