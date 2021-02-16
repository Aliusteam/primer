a=open('3.txt')
b=''
for line in a:
    b+=str(line).strip()
b=b.lower().split()
x=0
k=1
c1=[]
while len(b)!=0:
    c1.append(str(b.count(b[x]))+b[x])
    t=b[x]
    while t in b:
        b.remove(b[x])
        