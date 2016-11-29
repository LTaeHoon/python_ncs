'''
변수(variable) : 데이터를 저장하는 역할

'''
print('변수 선언과 초기화')

var1 ='Hello python' #"" or ''
print(var1)
print(type(var1)) 
'''
1. python 변수?
 - 값 or 주소를 저장하는 역할
 - 값 저장(java,c)
 - 주소 저장 (python) -> 참조변수
 - 가장 최근 값 저장
 - 데이터 형에 따라 타입이 결정
2. 변수명 규칙
 - 첫자 영문자, 두번째 (숫자, 특수문자(_))
 - 대문자, 소문자 구분(Num != num)
 - 숫자, 키워드(명령어) 사용불가(한글 비권장)
 
'''

var1 = 150; print(var1)
print(type(var1))
Num = 10; num=100
print(Num, num)

#키워드(명령어) 확인

import keyword   #외부에서 만들어진 모듈 import
print('키워드:', keyword.kwlist)

#참조변수
a = 250 # a는 250을 가리키는 주소를 갖고 있음, 250 저장 주소
b = 35.12 #35.12 저장 주소
c = b #동일 주소
d = 250 #이미 250이 있으면 중복해서 만들지 않고 원래 있던 해당 주소값을 d에 할당, 즉 a 주소 리턴

print(a,b,c,d) #250 35.12 35.12 250
#변수의 주소보기
print(id(a), id(b),id(c),id(d))
#1709827952 1540408 1540408 1709827952

'''
참조변수: 값(객체)의 주소를 저장한 변수
'''

#변수의 내용 비교 : 관계 연산자 사용
print(a==250) #True
print(a>=250) #True
#변수의 주소 비교 : is 키워드 사용
print(a is d) #True
print(b is c) #True
print(c is a) #False
