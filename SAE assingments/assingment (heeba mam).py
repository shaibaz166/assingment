x=input('enter a sentence-')
y=input('enter a word-')
s=x.lower()
w=y.lower()
l=s.split()
if w in l:
    print(l.count(w))
else:
    print('given word is not present')
