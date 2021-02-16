# задача https://stepik.org/lesson/3378/step/2?auth=login&unit=961
# Решение 1
s=open('8.txt')
a=s.readline().strip()
print(a)

import requests
r=requests.get(a)
print(r.text)
i=0
for x in r.text.splitlines():
    i+=1
print(i)
 #   print(x.splitlines())


# Решение 2
# import requests
#
# s=open('8.txt')
# a=s.readline().strip()
# print(a)
#
# r=requests.get(a)
# print(r.text)
# #print('-----------------')
# i=0
# # r=r.splitlines()
# #print(r)
# for x in r.text:
#  #   x=x.splitlines()
#     print(x,end=(''))
#     if x=='\n':
#         i+=1
# print(i)

# q=len(r.text)
# print(q)

# w=open('a')
# s1=w.readline()
# print(s1)

# for q in a:
#     print(q.strip())

#rint(requests.get(a))