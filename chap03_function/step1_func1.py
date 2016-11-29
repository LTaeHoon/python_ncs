'''
함수(Function)
 - 내장함수, 사용자 정의함수
 - 내장함수 : python 제공 함수
   -> 함수 호출) 함수([인수])
 - 사용자 정의함수
   형식) 
   def 함수명([인수]):
       실행문
       실행문
    [return <반환값>]

[] 표현 : 생략가능함

'''
from math import sqrt

'''
라이브러리 추가방법

#import 모듈
import statistics #방법1 : 모듈만 추가시 함수 사용시 모듈.함수()
#from 모듈 import 함수
from statistics import mean #방법2 : 함수 사용시 함수명만 쓰면 됨


'''



#1. 내장함수

from statistics import mean
#import statistics

dataset =[1,2,3,4,5]

print('합:',sum(dataset))
print('평균:',mean(dataset)) #모듈 추가
print('최소값:',min(dataset))
print('최댓값:',max(dataset))
print('길이:',len(dataset))

#문자열 -> 수식(코드) 변경함수
a=10.5
b=eval('a+3.14547')
print('b:',b) #b:13.64547
print(round(b,2)) #13.65

# 2.사용자 정의함수

#1) 인수가 없는 함수
def userfunc1():
    print('userFunc1')

#함수호출
userfunc1()
userfunc1()

#2) 인수가 있는 함수
def userFunc2(name): #가인수 = 매개변수
    print('hello,',name,'!!')
    
userFunc2('taehoon') #실인수
userFunc2('유관순')        

# 3) 리턴이 있는 함수
def userFunc3(a,b=100):
    calc = a+b
    return calc
'''
a = int(input('첫번째 수 입력:'))
b = int(input('두번째 수 입력:'))

result=userFunc3(a, b) #함수 호출
print('반환값:',result)
'''

result = userFunc3('안녕하세요.','홍길동입니다.')
print('반환값:',result)

result = userFunc3(10)
print('반환값:',result) #반환값 : 110

result = userFunc3(10,90)
print('반환값:',result) #반환값: 100


#분산, 표준편차 계산 
dataset = [5,9,1,7,4,6]

#분산 = sum((변량 - 산술평균)^2)/(n-1)
#표준편차 = sqrt(분산)

#평균 계산 함수
def avg_func(x):
    tot = sum(x) #합계
    l= len(x) #개수
    avg = tot/l
    return avg

avg =avg_func(dataset)
print('평균:',round(avg,3))

#분산,표준편차 함수 정의
def var_sd_func(x):
    avg = avg_func(x)
    #list 내포 : 리스트 내에 for문이 들어간 형태
    diff = [(xx-avg)**2 for xx in x] #차
    var = sum(diff)/(len(x)-1) #합계 /(n-1)
    
    sd = sqrt(var)
   
    return var,sd #분산,표준편차 리턴

var, sd =var_sd_func(dataset)
print('분산:',round(var,3))
print('표준편차:',round(sd,3))

#list 내포 = list + for
price = {'사과':2000,'복숭아':3000,'딸기':2500}
buy = {'사과':3,'딸기':5}

#구매 상품 총금액
#형식) 변수 = [실행문  for 변수 in 자료구조 ]
bill = [price[k]*buy[k] for k in buy] #list타입으로 리턴
print(bill) #[6000, 12500]
print('총 금액:',sum(bill))

