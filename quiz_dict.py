questions = {
    'Who founded Python?':'Guido Van Rossum', 
    'What is the shortened version of "boolean" in Python?':'bool', 
    'What is 23+71?':'94', 
    'When was Python created?':'1991', 
    'To assign a vsariable, do we use = or ==?':'='
}

score = 0

for question, answer in questions.items():
    your_answer = input(question + ': ')
    if your_answer == answer:
        score += 1
        print ('Well done!!')
    else:
        print ('LOOOOSER!!!!!')

print (f'Your final score is {score}')