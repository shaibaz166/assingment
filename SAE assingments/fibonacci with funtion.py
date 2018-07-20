#n=int(input('enter a number-'))
def fib(n):
    #n=int(input('enter a number-'))
    a=0
    b=1
    print(a,b)
    for i in range(n-1):
        c=a+b
        print(c)
        a,b=b,c
n=int(input('enter a number-'))
fib(n)
