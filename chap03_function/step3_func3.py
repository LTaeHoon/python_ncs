'''
1.축약함수(Lambda)
 -Lambda: 한 줄 함수를 의미
 형식) 함수명 = lambda 가인수 : 리턴값
 호출:함수명(실인수)

2.중첩함수
 형식)
 def outer():
     실행문
     def inner():
         실행문
         
         
'''

#사용자 정의함수
def Adder(x,y):
    #calc = x +y
    return x+y

result = Adder(10,20)
print('계산 결과:',result)

#Lambda 함수를 정의하시오.
myAdder = lambda x,y:x+y
print('계산 결과:',myAdder(10,20)) #함수 호출

#Lambda에서 가변인수 예
result = lambda dan, su = 5:dan*su
print(result(5000))

result2 = lambda dan,*su,**product:print(dan,su,product)
result2(1000,3,5,a=2500,b=3000)

# 2.중첩함수
def main_func(value):
    main_var = value #변수 초기화
    
    print(main_var)
    def plus(x1,x2):
        result = x1 + x2
        return result
    def minus(x1,x2):
        result = x1 - x2
        return result
    def getMain_var(): #getter():획득자
        nonlocal main_var #지역변수 아님(main에서 선언된 outer 변수)
        return main_var #값 반환
    def setMain_var(value): #setter():지정자
        nonlocal main_var
        main_var = value #변수에 값을 변경
    return plus, minus, getMain_var,setMain_var

p,m,g,s = main_func(100) #outer 함수 호출 -> inner 함수 리턴 받음
result = p(100,200) #덧셈
print('덧셈 결과:', result) #덧셈 결과: 300
result2 = m(500,250) #뺄셈
print('뺄셈 결과:', result2) #뺄셈 결과: 250
#getter() 함수 : 확인
print('get 함수 :',g()) #get함수 : 100
#setter() 함수 : 변경
s(1000)
print('get 함수 :',g()) #get함수 : 1000




