a=input('enter a sentence-')
b=input('enter a word to be remove-')
s=a.lower()
w=b.lower()
l=s.split()
e=w.split()
y=[]
for i in l:
    if i in e:
        y.append(i)
        l.remove(i)
        x=" ".join(l)
    else:
        print('word is not present')
        
#x=" ".join([y for y in l if y not in e ])

