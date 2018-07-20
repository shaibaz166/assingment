D2,b,c={'Maths':78,'Chem':76,'Phy':64,'Mech':64,'Java':67},0,999999999
print(D2)
D1=list(D2.values()) 
for each in D1:
 if each>b:
     b=each
 else:
     b=b
 if(each<c):
     c=each
 else:
     c=c

print('Maximum Value in a Dctionary: ',b)
print('Minimum Value in a Dctionary: ',c)

'''D={'maths':78,'chem':76,'phy':77,'mech':67,'java':72}
marks=list(D.values())
marks.sort()
Max=marks[len(marks)-1]
Min=marks[0]
print(Max)
print(Min)
'''
