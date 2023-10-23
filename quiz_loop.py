questions = ['Who founded Python?', 'What is the shortened version of "boolean" in Python?', 'What is 23+71?', 'When was Python created?', 'To assign a vsariable, do we use = oe ==?']
answers = ['Guido Van Rossum', 'bool', '94', '1991', '=']

score = 0
index = 0

for question in questions:
    your_answer = input(question + ': ')
    if your_answer == answers[index]:
        score += 1
        print ('Well done!!')
    else:
        print ('LOOOOSER!!!!!')
    index += 1

print (f'Your final score is {score}')