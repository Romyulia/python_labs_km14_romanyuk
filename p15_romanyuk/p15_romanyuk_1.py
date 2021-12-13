from math import factorial
while True:
    degree = input('Enter the degree of a polynomial: ')
    if degree.isdigit():
        degree = int(degree)
        break

for n in range(degree + 1):
    b = (round(factorial(n)/(factorial(k)*(factorial(n-k)))) for k in range(n + 1))
    for j in b:
        print(j, end = ' ')
    print()