w={}
s=open('10.txt')
i=0
for x in s:
    x=x.strip()
#    print(x)
    x=x.split()
#    print(x[0])
    if x[0] not in w:
        w[x[0]]=x[2]
    elif x[0] in w:
        w[x[0]]+=' '
        w[x[0]]+=x[2]
    continue
#print(w)
v=[]
d=0
for x,y in w.items():
    q=len(y.split(' '))
#    print(q)
    for k in y.split(' '):
        d+=int(k)
#    v.append([int(x),round(d/q)])
    v.append([int(x), d / q])
#    v[x]=float(d/q)
#    print(x,float(d/q))
    d=0
v.sort()
print(v)
i=1
for x,y in v:
    if x==i:
        print(x,y)
    else:
        print(i, '-')
    i+=1