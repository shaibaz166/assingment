s=input('enter a sentence')
#w=input('enter a word')
w=['is','are','am','of','as','on','a']
l=s.lower().split()
#e=w.split()
y=[]
for i in l:
    if i in w:
        y.append(i)
        l.remove(i)
x=" ".join(l)
print(x)
