'''
Created on 2016. 11. 30.

@author: acorn
'''
from operator import index

'''
문제1) 서울 지역 주소만을 대상으로 '동‘의 전체 개수를 출력하시오.
<조건1> 중복되는 '동' 제외
<조건2> 전체 '동' 개수 출력
'''
'''
x = [1,2,3,1,2,4]
print(x)

#list -> set변경 : 중복값 제거됨
sx = set(x)
#set -> list 변경
xx = list(sx)
print(sx,xx)
'''
import os

donglist =[]
cnt =0
try :
    file = open('C:/NCS/python/workspace(python)/chap04_FileIO/data/zipcode.txt',mode='r',encoding='utf-8')
    lines = file.readline() #첫번째 줄 읽기
    while lines:
        line = lines.split('\t')
        if line[1]=='서울':
            dong=line[3].split(' ')   #스페이스로 구분
            donglist.append(dong[0])   #스페이스 앞 값만 동리스트에 입력
           
        lines = file.readline()
    
    file.close()
    dongset = set(donglist) #자료구조 set으로 변환하여 중복값 제거
    dongli =list(dongset)  #자료구조 list로 변환
         
    print('서울특별시 전체 동의 개수 =', len(dongli))
    dongli.sort()
    
    for i in dongli:
        if (dongli.index(i)+1)%10 ==0:
            print('['+i+']');  
        else :
            print('['+i+']', end=' ') #같은 줄에 반복
except FileNotFoundError as e:
    print('Error 발생 :',e)
 

