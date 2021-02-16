e=[] # список в списке
for m in range(3):
    c={}
    d=[]
    b=input('')
 #   print(b)
    a=b.split(';')
    for x in a:
        if x.isalpha():
            c[x]=0
 #           print(c)
        elif x.isdigit():
            d.append(x)
    e.append(d)
 #   print(d)
    for x,y in c.items():
        if y==0:
            c[x]=d
    print(c)
print(e)
for x in e:
    g=0 # сумма чисел
    i=0 # кол-во чисел
    for y in x:
        g+=int(y)
        i+=1
    print(g/i)
    
g=0 # сумма чисел
i=0 # кол-во чисел
h=len(e)
k=0
for y in range(h):
    g=0
    i=y
    for x in range(h):
        g+=(int(e[x][i]))
    print(g/(x+1),end=(' '))
