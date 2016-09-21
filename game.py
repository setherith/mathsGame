import random

for attempts in range(1, 11):

    types_of_questions = ['subtraction', 'addition', 'multiplication', 'division']

    question_type = types_of_questions[random.randint(0, 3)]

    a = random.randint(1, 12)
    b = random.randint(1, 12)

    print(question_type)

    if question_type == 'addition':
        x = input('What is ' + str(a) + ' + ' + str(b) + ' = ? ')
        if int(x) == a + b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == 'subtraction':
        x = input('What is ' + str(a) + ' - ' + str(b) + ' = ? ')
        if int(x) == a - b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == 'multiplication':
        x = input('What is ' + str(a) + ' x ' + str(b) + ' = ? ')
        if int(x) == a * b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == 'division':
        x = input('What is ' + str(a) + ' % ' + str(b) + ' = ? ')
        if int(x) == a / b:
            print('Correct!')
        else:
            print('Wrong!')