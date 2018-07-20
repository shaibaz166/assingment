def palindrome(n):
    rev,value_user=0,n
    while(n!=0):
        r=n%10
        rev=rev*10+r
        #print(rev)
        n=n//10
    print(rev)
    if(value_user==rev):
        print('number is plaindrome')
    else:
        print('Number is not palindrome')
n=int(input('enter a syntax'))
palindrome(n)
