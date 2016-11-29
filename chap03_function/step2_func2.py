'''
함수의 가변 인수
 형식) 함수명(*가변인수)
 - 여러 개의 실인수를 받을 수 있는 인수
 - tuple type으로 받는다.
 
'''

def Func1(name1,*name2):
    print(name1,name2) #홍길동 ('이순신', '유관순')
    print(type(name2)) #<class 'tuple'>
    for n in name2:
        print(n)
    
Func1('홍길동','이순신','유관순')

# 통계량을 구하는 함수
def statics(Func,*data):
    if Func =='sum':
        print(sum(data))
    elif Func =='max':
        print(max(data))
    elif Func =='mean':
        tot = sum(data)
        l = len(data)
        print(tot/l)    


statics('sum',3,2,5,12.5,78) #100.5
statics('max',3,2,5,12.5,78) #78
statics('mean',3,2,5,12.5,78) #20.1

#형식) 함수(**가변인수) -> dict type으로 받는다.

def person(w,h,**other):
    print('몸무게:',w) #몸무게: 65
    print('키:',h) #키: 180
    print('기타:',other) #{'name': '홍길동', 'age': 35}
    
person(65,180,name='홍길동',age=35)



