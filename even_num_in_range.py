a = int(input('Enter a number '))
b = int(input('Enter a second number bigger than the first '))

if a > b:
    b = int(input('You screwed up, enter a number BIGGER than the first '))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)