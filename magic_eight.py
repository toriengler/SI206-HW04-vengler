def ask_question():
    ask=input ('What is your question? ')
    while ask!= 'quit':
        if ask[-1] !='?':
            print("I’m sorry, I can only answer questions.")
            ask=input ('What is your question? ')

        questions=[]
        save= questions.append(ask)
        ask=input ('What is your question? ')


ask_question()
