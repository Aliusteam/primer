# 8	Larkins	166
# 9	Conors	171
# 4	Jones	144
# 8	Leapman	161
# 1	Timmons	130
# 3	Owen	138
# 7	Mercer	158
# 10	Backer	171
# 5	Gardner	144


1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0


# Вывод программы
# Команда:
#
# Всего_игр
# Побед
# Ничьих
# Поражений
# Всего_очков
#
# # 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2

# Sample Output:
#
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1


'''
r='wert asd asd'
if a[0]+a[1]=='we':
    print('ok')

s=open('9.txt')
a=s.readline()
print(a)
import requests
w=requests.get(a)
print(w)

# q=requests.get(w)
# print(q)
#
q=w.readline()
#
# print(q)



Имеется набор файлов, каждый из которых,
кроме последнего, содержит имя
следующего файла.
Первое слово в тексте последнего файла:
"We".

Скачайте предложенный файл. В нём
содержится ссылка на первый файл из
этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/
course67/3.6.3/

Загрузите содержимое ﻿последнего файла
из набора, как ответ на это задание.



import requests
r=requests.get('http://muzlove.ru')
print(r.text)
print('--------')
import requests
url='http://muzlove.ru'
pair={'one':'qwerty','thue':'asdfg'}
r=requests.get(url, pair)
print(r.url)




# import requests
# url = 'http://httpbin.org/cookies'
# cookies ={'cookies_are': 'working'}
# r = requests.get(url, cookies=cookies) # отправка сформированных cookies на сервер
# print(r. text)

# import requests
# r=requests.get('https://optolist.ru')
# print(r.text)



# import sys
# print('\n'.join(sys.argv[1:]))

# import subprocess
# subprocess.call('ipconfig')


# # import sys
# # print('privet')
# # # print(len(sys.argv))
# # print(sys.argv[1:])
# # #print(sys.argv[1])
# # s=len(sys.argv)
# # if s>1:
# #     print('Нажми:',input('') )
# # else:
# #     print('oooooOOOnoooo')
# #
# # # for i in range (sys.argv):
# # #     print(sys.argv[i+1])
# #
#
# # python3 my_solution.py arg1 arg2
# # arg1 arg2
#
# # import sys
# # print(*sys.argv[1:])
# #
# # import sys
# # print(' '.join(sys.argv[1:]))
#
#
# #print(sys.argv[1])
#
#
# # for x in sys.argv[1:]:
# #     print(x,end=(' '))
#
# # import subprocess
# # print(subprocess.call('ipconfig', shell=True))
#
# # a='sdfasdfasd'
# # print(a[4])
#
#
'''