import random
import time
from init import Config


config = Config()


def generate_range():
    return random.randint(config.min_val, config.max_val), random.randint(config.min_val, config.max_val)


def question(operator, operand_a, operand_b):
    """Build the question string"""
    return 'What is ' + str(operand_a) + ' ' + operator + ' ' + str(operand_b) + ' = ? '

total_time = 0

for attempts in range(1, config.no_questions + 1):

    start_time = time.time()

    types_of_questions = ['-', '+', 'x', '÷']

    question_type = types_of_questions[random.randint(0, 3)]

    a, b = generate_range()

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

    end_time = time.time()
    diff = round(end_time - start_time, 2)
    total_time += diff
    print(str(diff) + " seconds")

total_time = round(total_time, 2)
average = round(total_time / config.no_questions, 2)
print("Total time taken: " + str(total_time))
print("Average: " + str(average))
