import random


def question(operator, operand_a, operand_b):
    """Build the question string"""
    return 'What is ' + str(operand_a) + ' ' + operator + ' ' + str(operand_b) + ' = ? '

for attempts in range(1, 11):

    types_of_questions = ['-', '+', 'x', '÷']

    question_type = types_of_questions[random.randint(0, 3)]

    a = random.randint(1, 12)
    b = random.randint(1, 12)

    if question_type == '+':
        x = input(question('+', a, b))
        if int(x) == a + b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == '-':
        x = input(question('-', a, b))
        if int(x) == a - b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == 'x':
        x = input(question('x', a, b))
        if int(x) == a * b:
            print('Correct!')
        else:
            print('Wrong!')

    if question_type == '÷':
        # Alt + 246 = '÷'
        while (a / b) % 1 != 0:
            a = random.randint(1, 12)
            b = random.randint(1, 12)

        x = input(question('÷', a, b))
        if int(x) == a / b:
            print('Correct!')
        else:
            print('Wrong!')
