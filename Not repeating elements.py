x=input()
l=x.split()
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
print(l1)
