import random

def question(operator, operandA, operandB):
    """Build the question string"""
    return 'What is ' + str(operandA) + ' ' + operator + ' ' + str(operandB) + ' = ? '

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
        x = input(question('÷', a, b))
        if int(x) == a / b:
            print('Correct!')
        else:
            print('Wrong!')
