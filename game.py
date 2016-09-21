import random

for attempts in range(1, 11):
    a = random.randint(1, 12)
    b = random.randint(1, 12)

    x = input('What is ' + str(a) + ' + ' + str(b) + ' = ? ')
    if int(x) == a + b:
        print('Correct!')
    else:
        print('Wrong!')

