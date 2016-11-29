'''
반복문(while)

형식)
while 조건식:
    실행문
    실행문
'''
a = 1
t = 0
while a<=5:
    print(a,end=' ') # 1 2 3 4 5
    a+=1 #a=a+1
    t+=a #t=t+a a값을 누적(누적변수)
    print(t,end=' ')
     
print() #line skip (줄바꿈)
# 1~100 사이 중 5의 배수의 합을 구한다.

i=1
t=0

while i<=100: #100회 반복
    if i%5 ==0:
        t+=i #누적변수
    i+=1 #카운터
    
print('1~100사이 중 5의 배수의 합은 %d이다.'%t)

#1~100 사이에서 3의 배수이면서(and) 2의 배수가 아닌 합을 출력하시오.
i=1
t=0

while i<=100:
    if i%3==0 and i%2!=0 :
        print(i,end=' ')
        t+=i
    i+=1
print()
print('1~100 사이에서 3의 배수이나 2의 배수가 아닌 합은 %d이다.'%t)

#문2) -1,3,-5,7,-9 ~ 99

i=1
t=0
cnt = 0
while i<100 :
    if i%2!=0 : #홀수이면
        cnt+=1  #수열의 위치 판단
        if cnt%2!=0 : #수열의 위치가 홀수 이면
            k=-1*i    #부호변경
            t+=k      #누적합
        else:#짝수 위치
            t+=i     
        
    i+=1
    
print('t=%d'%t) #t=50

#무한 루프 -> 반복문 안에 반드시 exit 조건 지정
while True:
    a = int(input('숫자 입력:'))
    if a==0: #exit 조건
        print('프로그램 종료')
        break #탈출
    print('입력 값 ->',a)
    
import random

names =['홍길동','이순신','유관순']
print(names,names[2])

#모듈.함수()
r=random.randint(0,2) #0~2사이의 난수 정수 발생

print(names[r])

# input == r : 성공 (exit), input > r :'더 작은 수 입력', input <r :'더 큰수 입력'
'''
r = random.randint(1,10)
while True:
    print('숫자 맞추기 게임')
    i = int(input('예상 숫자를 입력하시오:')) #숫자 입력
    if i==r:
        print('성공!!')
        break
    elif i > r:
        print('더 작은 수 입력')
    elif i < r:
        print('더 큰수 입력')
'''        
'''
continue, break
'''
a = 0
while a<10 :
    a+=1 #카운터
    if a==3:continue # 1 2 4 다음 문장 skip
    if a>=5:break #1 2 3 4 -> exit
    print(a, end=' ') #1 2 3 4 5 6 7 8 9 10
     


        
