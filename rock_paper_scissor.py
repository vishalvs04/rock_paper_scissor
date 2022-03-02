import random
def play_rock_paper_scissor():
    runner_code=True
    user_score=0
    comp_score=0
    while runner_code:
        choices=['rock','paper','scissor']
        user_choice=input("Choose Rock, Paper or Scissor, OR q/Q/quit/Quit/QUIT for quitting: ")
        computer_choice=random.choice(choices)

        if user_choice==computer_choice:
            print('Its A TIE!!!!')
        elif user_choice=='rock' and computer_choice=='paper':
            print('Paper covers Rock, Computer Wins')
            comp_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='scissor' and computer_choice=='rock':
            print('Rock Breaks Scissor, Computer Wins')
            comp_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='paper' and computer_choice=='scissor':
            print('Scissor Cuts Paper, Computer Wins')
            comp_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='paper' and computer_choice=='rock':
            print("Paper Covers Rock, User Wins")
            user_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='rock' and computer_choice=='scissor':
            print('Rock breaks Scissor, User Wins')
            user_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='scissor' and computer_choice=='paper':
            print('Scissor cuts paper, User Wins')
            user_score+=1
            print('User Score=',user_score)
            print("Computer's Score=",comp_score)
        elif user_choice=='quit' or user_choice=='q' or user_choice=='Quit' or user_choice=='QUIT' or user_choice=='Q':
            if user_score>0 or comp_score>0:
                print('User Score=',user_score)
                print("Computer's Score=",comp_score)
            print('Quit')
            runner_code=False