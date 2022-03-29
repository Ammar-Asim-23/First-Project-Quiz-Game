#MAIN FUNCTION
def playing(subject,answers):
        '''
        Main funtion which takes data from Quiz Bank and takes the Quiz.
        Calculates and tell the score in the end.
        It takes two arguments, Question Bank and Answer Bank.
        '''
        import random
        random_num=[]
        score=0
        hq=open(subject)
        ha=open(answers)
        Qstrings=hq.read()
        Astrings=ha.read()
        Answers=Astrings.split('_')    
        Question_prompt=Qstrings.split('_')
        
        i=1
        while i < 11: 
            num_=random.randint(0,len(Question_prompt)-1)
            if num_ not in random_num:
                random_num.append(num_)
                i+=1           
        i=1
        
        for j in random_num:   
            print(f'Question # {i}')
            user_answer=input(Question_prompt[j])
            i+=1
            if user_answer == Answers[j]:
                print('Correct Answer')
                score+=1
            else:
                print('Wrong Answer')
        print(f'Your final score is {score}/10.')
        print('Thank you for playing......\nPlease play again')
        hq.close()
        ha.close() 

#MIX FUNCTION
def mix_play(sub_1,ans_1,sub_2,ans_2):
    '''
    Function to take Quiz from two Quiz Banks at the same time.
    It takes four arguments, "Question Bank_1 and Answer Bank_1" 
    and "Question Bank_2 and Answer Bank_2".
    '''
    
    import random
    random_num=[]
    score=0
    hq=open(sub_1)
    ha=open(ans_1)
    hq_2=open(sub_2)
    ha_2=open(ans_2)
    Qstrings=hq.read() +'_'+ hq_2.read()
    Astrings=ha.read() + ha_2.read()
    Answers=Astrings.split('_')    
    Question_prompt=Qstrings.split('_')
    i=1
    while i < 11: 
        num_=random.randint(0,len(Question_prompt)-1)
        if num_ not in random_num:
            random_num.append(num_)
            i+=1               
            
    i=1
    for j in random_num:   
        print(f'Question # {i}')
        user_answer=input(Question_prompt[j])
        i+=1
        if user_answer == Answers[j]:
            print('Correct Answer')
            score+=1
        else:
            print('Wrong Answer') 
    print(f'Your final score is {score}/10.')
    print('Thank you for playing......\nPlease play again')
    hq.close()
    ha.close()    

#ADMIN FUNCTION
def add(sub,ans):
    '''
    Function to add Questions in a selected Quiz bank.
    It takes two arguments, Question Bank and Answer Bank.
    '''
    hq=open(sub,'a')
    ha=open(ans,'a')
    while True:
    #Write a new question with three options using \n character.Leave a \n at end
        hq.write('_'+(input('Add new Question,Please donot use _ character, use & for new line\n')))
        hq.write('\n(a) '+(input('Enter option a.')))
        hq.write('\n(b) '+(input('Enter option b')))
        hq.write('\n(c) '+(input('Enter option c.')))
        hq.write('\n(d) '+(input('Enter option d.'))+'\n')
    #Write the answer of new question
        ha.write(input('Add answer of question')+'_')
        Quit=input('Do you want to quit(q).Press any other key to continue\n ')
        if Quit == 'q':
            hq.close()
            ha.close()
            break
def view(sub,ans):
    '''
    Function to view all the questions and answers 
    stored in the question bank.
    '''        
    hq=open(sub)
    ha=open(ans)
    Qstrings=hq.read()
    Astrings=ha.read()
    Answers=Astrings.split('_')    
    print(Qstrings)
    print(Answers)


      