
import random,time,sys
class dice():
    def five(self):
        for i in range (2,0,-1):
            for j in range(2,i,-1):
                print(" ",end="")
            for j in range(i):
                print("*",end=" ")
            print()
        for i in range(1,2):
            for j in range(2,0,-1):
                print('*',end=" ")
            print()

#print 1 dice numbers
    def one(self):
        for i in range(3,0,-1):
            for j in range(3,i,-1):
                print(' ',end="")
            if i==2:
                print('*',end="")
        print()

#four number
    def four(self):
        for i in range(1,4,2):
            for j in range(1,4,2):
                print('*',end=" ")
            print()

#three number
    def three(self):
        for i in range(1,4):
            for j in range(1,i+1):
                if j==i:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()
#six number
    def six(self):
        for i in range(1,4):
            for j in range (1,4,2):
                print("*",end=" ")
            print()

    def two(self):
        for i in range(1,4):
            for j in range(1,i+1,2):
                if j==i:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()




count,u,c=0,0,0
diceroll=dice()
print('\nRules')
def loading():
    print("\nSumming A Value ",end=" ")
    animation="..."
    for i in range(3):
        time.sleep(2.5)
        sys.stdout.write("\r"+animation[i%len(animation)])
        sys.stdout.flush()
    print("\nResult are")

def Result():
    print("\nNow its time for Rolling Dices",end="")
    animation="..."
    for i in range(3):
        time.sleep(2.5)
        sys.stdout.write("\r"+animation[i%len(animation)])
        sys.stdout.flush()
while True:
    print("guess a sum of two rolling dices")
    count=count+1
    try:
        n=int(input())
    except ValueError:
        print("Enter a Number Value")
        n=int(input())
    while n>12 or n<2:
        n=int(input("enter a valid sum number"))
    Result()
    print()
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    s=dice1+dice2
    if dice1==1:
        print()
        diceroll.one()
        
        
    elif dice1==2:
        print()
        diceroll.two()
        
        
    elif dice1==3:
        print()
        diceroll.three()
        
    elif dice1==4:
        print()
        diceroll.four()
        
    elif dice1==5:
        print()
        
        diceroll.five()
        
    elif dice1==6:
        print()
        diceroll.six()
    if dice2==1:
        print()
        
        diceroll.one()
        
    elif dice2==2:
        print()
        
        diceroll.two()
        
    elif dice2==3:
        print()
        
        diceroll.three()
        
    elif dice2==4:
        print()
        
        
        diceroll.four()
        print()
        
    elif dice2==5:
        print()
        
        diceroll.five()
        
             
        print()
        
    elif dice2==6:
        print()
        
        diceroll.six()
        
    loading()
    print(s)
    if s==n:
        print("\nUser win this round")
        u=u+1
    else:
        print("\nComputer win this round")
        c=c+1
    print("Do YOu Want to Play Again")
    ans=input()
    ans1=ans.lower()
    while ans1!="y" and ans1!="n":
        ans=input("enter valid option")
        ans1=ans.lower()
    if ans1=='n':
        break
    if count==4:
        print("Your Chances are Finish")
        if u>c:
            print('User is Winner')
            break
        elif u==c:
            print('This is Draw')
            break
        else:
            print('Computer is going to WIN')
            break
print("\nGame Over\nThanks for Playing")

