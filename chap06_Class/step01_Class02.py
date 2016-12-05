'''
묵시적 생성자 = 기본 생성자
- 생성자를 정의하지 않으면 기본으로 생성되는 생성자

'''

# 단계1 : 클래스 정의
class TV :
    #1. 멤버변수 : 명사
    channel = 0 # 채널
    power = False #False(off)/True(on)
    color = '없음' #TV color
    
    #2. 생성자 : 묵시적 생성자 -> 객체만 생성하는 역할
    def __init__(self):
        pass #내용 없음을 의미
    #3. 함수(기능 정의) : 동사
    def display(self): #TV 정보 출력하기
        print('채널상태 : {0}이고, 전원상태:{1},색상:{2}'.\
              format(self.channel, self.power,self.color))
    def color_change(self,color):
        self.color = color
            
    def powerOn_Off(self): #전원 스위치
        self.power = not(self.power) #토글 : F->T, T->F
    
    def channel_UP(self): #채널 올리기
        self.channel +=1 #1씩 증가
    
    def channel_DOWN(self): #채널 내리기
        self.channel -=1 #1씩 감소
        
#단계 2: 객체 생성(묵시적 생성자)
t1 = TV() #묵시적 생성자로 객체 생성

#단계 3: 참조변수 이용 멤버 참조
t1.display()

#전원 On
t1.powerOn_Off()
#채널 올리고
t1.channel_UP()
#TV 정보 출력
t1.display()

#TV 색상 변경
t1.color_change("빨강")
t1.display()

'''
문)tv2객체를 다음과 같이 생성하시오
조건1) 전원 on
조건2) 채널 11변경 -> 5번으로 변경
조건3) 색상 검정
조건4) TV 정보 출력하기
'''
t2 = TV()
t2.display()
t2.powerOn_Off()
for i in range(11): #0~10 :11번 채널up 호출
    t2.channel_UP()
t2.color_change("검정")
t2.display()

for j in range(6): #0~5 : 6회 반복
    t2.channel_DOWN()
t2.display()
    
