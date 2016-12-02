'''
step01_Class01

'''


'''
클래스(Class) ?
 - 객체를 생성하는 자료구조(data 저장 틀)
 - 구성요소 : 멤버(member), 생성자
 - 멤버 : 변수(data 저장) + 함수(기능 정의)
 - 생성자 : 객체를 생성하는 역할(함수 구조 동일) 
 
형식)
class 클래스명 :
   1.변수 선언 = 초기화  -> data 저장 역할
   2.생성자             -> object 생성
   3.def 함수명(인수): -> 기능 수행
         실행문
         
객체 생성 과정
1. class 정의 -> 2.Object 생성(생성자를 이용해): 객체는 메모리에 저장 -> 3. 참조변수(객체의 주소를 갖고 있음)

참조변수 = Class생성자() #Object 생성

클래스 유형 : 사용자 정의 클래스, 내장 클래스         
'''

# 1. 함수 정의
def Adder(x,y): #매개변수
    add=x+y #지역변수 : add, x, y
    return x,y,add
    
# 함수 호출
x,y,add=Adder(10,20) #실인수
print(x,'+',y,'=',add)

# 2.사용자 정의 클래스

# 단계1: 클래스 정의
class Today:
    # [1.변수] : data 저장 : 명사
    year = None #null
    month = None
    day =None
    # 2.생성자 : 객체 생성 역할(함수 유사)   
    def __init__(self,year,month,day): #1.객체 생성 +2. 멤버변수 초기화
        self.year = year
        self.month = month
        self.day = day
        
    # [3.멤버함수] : 기능 정의 : 동사 
    def display(self):
        print('%d년 - %d월 - %d일'%(self.year,self.month,self.day))
        
# 단계2: 객체 생성(생정자 이름)
today = Today(2016,12,2) # 생성자 이용 객체 생성
#형식) 참조변수 = 생성자(실인수)

# 단계3: 참조변수 이용 멤버(변수+함수) 호출
# 참조변수.멤버(변수, 함수)
today.display() #2016년 - 12월 - 2일
print(today.year,today.month,today.day) #2016 12 2

# 두번째 객체 생성
today2 = Today(2016,12,3)
#참조변수.멤버
today2.display()
print(today2.year, today2.month, today2.day)

#객체 주소 확인
print(id(today),id(today2))

# 3. 내장 클래스(python 제공)

#import 패키지명.모듈명.함수()
import datetime #datetime.py(함수, 클래스)

#생성자 이용 Object 생성 -> 참조변수 주소 리턴
today3 = datetime.date(2016,12,2)
#help(datetime.date)

#참조변수.멤버(변수)
print(today3.year,today3.month,today3.day) #2016 12 2

#참조변수.멤버(함수)
w = today3.weekday() #0-4:평일 5~6:주말

if w>=5:
    print('주말입니다')
else :
    print('평일입니다')

# 단계1 :자동차 클래스 정의
class Car : 
    #1. 멤버 변수 : 클래스 자체에서 선언된 변수
    door = 0
    cc=0
    name=None
    #2. 생성자
    def __init__(self,door,cc,name):
        self.door = door
        self.cc = cc
        self.name = name
    
    #3. 멤버 함수 정의 
    def display(self):
        print('%s는 엔진이 %dcc이고 문짝은 %d개 이다.'%(self.name,self.cc,self.door))    

# 단계2 : 객체 생성
sonata = Car(4,2500,'NF 소나타')
benz = Car(4,2200,'benz E200')

# 단계3 : 참조변수 이용 자동차 정보 출력
sonata.display() 
#NF 소나타는 엔진이 2500cc이고 문짝은 4개 이다.
benz.display()
