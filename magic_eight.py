import random

def ask_question():
    ask=input ('What is your question? ')
    while ask!= 'quit':
        if ask[-1] !='?':
            print("I’m sorry, I can only answer questions.")
            ask=input ('What is your question? ')

        questions=[]
        save= questions.append(ask)
        ask=input ('What is your question? ')


def random_answer():
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

    return random.choice(answers)
