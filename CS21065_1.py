'''If file is not reading Quiz Func and Question Bank in Your Code Editor try to use the Open Folder
function in the code editor and try running again'''

from CS21065_2 import add, playing , mix_play , add, view

#Press a to run as administrator,p to play and q to quit

print('Welcome to Quiz Mania\nFun Fact: Did You know Playing Quiz Daily Sharpens your Brain.... ')
random_num=[]
score=0

#MODE SELECT
mode=input('Would You like to enter as administrator(a) or player(p) or quit(q)\n')

#ADMIN MODE
if mode == 'a':
    password=input('Please authenticate before entering:    ')
    
    if password == 'admin':
        print('Quiz Bank codes\n1. Computer\n2.Science')
        class_name=input('Which Quiz Bank do you want to change:    ')
        if class_name=='1':
            print("Would you like to add a question(a) or view questions(v)")
            adm=input()
            if adm == 'a':
                add('CS21065_3.txt','CS21065_4.txt')
            elif adm == "v":
                view('CS21065_3.txt','CS21065_4.txt')
            else:
                print('Wrong Choice')        
        
        if class_name=='2':
            print("Would you like to add a question(a) or view questions(v)")
            if adm == 'a':
                add('CS21065_5.txt','CS21065_6.txt')
            elif adm == "v":
                view('CS21065_5.txt','CS21065_6.txt')
            else:
                print('Wrong Choice')     
    
    else:
        print('Wrong Password')                    

#PLAYER MODE
elif mode == 'p':
    print('Quiz Bank Choices:\n1.Computer\n2.Science\n3.Mix')
    bank=input('Select Your Quiz Bank.(Use index number 1,2,3):      ')
    
    #BRAINTEASERS
    if bank == '1':
        playing('CS21065_3.txt','CS21065_4.txt')
    
    #GENERAL KNOWLEDGE
    elif bank == '2':
        playing('CS21065_5.txt','CS21065_6.txt')
    
    #MIX
    elif bank == '3':
        mix_play('CS21065_3.txt','CS21065_4.txt','CS21065_5.txt','CS21065_6.txt')

#QUIT
elif mode == 'q':
    print('We hope to see you again.')
    quit()

#WRONG CHOICE
else:
    print('Please enter a valid choice')                




      

