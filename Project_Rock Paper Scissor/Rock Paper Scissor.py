
u,c,count=0,0,0
import random,time,sys
def loading():
    print("Loading",end="")
    animation="..."
    for i in range(3):
        time.sleep(2.5)
        sys.stdout.write("\r"+animation[i%len(animation)])
        sys.stdout.flush()
    print("\nResult are")

def Result():
    print("\nNow its computer turn",end="")
    animation="..."
    for i in range(3):
        time.sleep(2.5)
        sys.stdout.write("\r"+animation[i%len(animation)])
        sys.stdout.flush()
        
print(''''These are the Rules:
\n 1-You have only 4 chances\n 2-If you scores or win more than 2 You become winner \n 3-You Know a game rules if you dont know then why are you here :P \n
if you dont know game rules than refer this-
            Rock vs paper->paper wins \n
            Rock vs scissor->Rock wins \n
            paper vs scissor->scissor wins \n
''')
time.sleep(1.5) 
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    count=count+1
    try:
        choice = int(input("User turn: "))
    except ValueError:
        print("Enter a Number between 1 to 3")
        choice=int(input())
 
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
     
    print("user choice is: " + choice_name)
    Result()
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
         
    print("\nComputer choice is: " + comp_choice_name)
 
    print(choice_name + " V/s " + comp_choice_name)
    time.sleep(0.1)
    loading()
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("\npaper wins ")
        result = "paper"
         
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("\nRock wins")
        result = "Rock"
    else:
        print("\nscissor wins")
        result = "scissor"
 
    if result == choice_name:
        print("\nUser wins")
        print('\nYou just win this round just chill its just Started\n')
        u=u+1
    else:
        print("\nComputer wins")
        print('\nYou Play with Wrong Person Man\n')
        c=c+1
    
    print("Do you want to play again? (Y/N)")
    ans = input()
    answer=ans.lower()
 
    while answer!='y' and answer!='n':
        ans=input('enter Y or N only')
        answer=ans.lower()
    if answer=='n':
        break

    if count==4:
        print("Sorry!!! You Got Only 4 Chances ")
        if c>=3:
            print("You Lost!But your tried so hard to win")
            break
        elif c==u:
            print('''ITS DRAW!\nYou Play Good''')
            break
        else:
            print("You Are Champion! and There is No Shame in losing to Champion")
            break
     
print("\nGAME OVER\nTHANKS FOR PLAYING")
time.sleep(5)
