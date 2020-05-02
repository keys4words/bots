def find_person(name):
    l = ['Jack', 'Maria', 'Sam', 'Den', 'Kelly', 'Peter']
    for el in l:
        if el == name:
            print(f'\t{name} is here')
        else:
            print(f'{el} is not {name}')

# find_person('Den')
answers = {
    'hey!': "> Hi, glad to see you",
    'how are you?': "> I'm fine",
    "what's up?": '> OK dude',
    'bye': '> See you'
}


def ask_user(answers):
    while True:
        question = input('Ask me something: ')
        answer = get_answer(question, answers)
        print(answer)
        if question == 'bye':
            break


def get_answer(question, answers):
    return answers.get(question, 'hmmm...')

try:
    ask_user(answers)
except KeyboardInterrupt:
    print("********** Sorry you leave **********")