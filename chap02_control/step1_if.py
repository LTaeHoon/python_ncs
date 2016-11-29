'''
제어문 (if)

'''

#키보드로 점수를 입력받아서 100~85 :'우수', 84~70:'보통', 69이하:'저조

score = int(input('점수입력:'))
if score >=100 :
    print('비유효숫자 입력')
else:
    if score >=85 and score <=100:
        print('우수')
    else:
        if score >= 70 and score <=84:
            print('보통')
        else :
            print('저조')
            
#시스템의 날짜/시간 가져오기
import datetime #모듈(함수,클래스) 포함

today=datetime.datetime.now() #모듈.클래스.함수()

print(today)
        
day = today.weekday()
print(day) #0~4: 월~금

if day >= 5 :
    print('오늘은 휴일')
else:
    print('오늘은 평일') # 3- 오늘은 평일
    
'''
형식3)
if 조건문1:
    실행문1
elif 조건문2:
    실행문2
else:
    실행문n
'''
    
#문1) 키보드로 점수를 입력받아서 100~85 :'우수', 84~70:'보통', 69이하:'저조
#조건 형식 3 적용

score = int(input('점수입력:'))
grade = ""
if score >= 85 and score <=100:
    #print('우수')
    grade='우수'
elif score >=70:
    #print('보통')
    grade='보통'
else:
    #print('저조')
    grade='저조'

print('당신의 점수는 %d이고 평가결과는 %s입니다.'%(score,grade))
 
num = 9 # 초기화   
result = 0
'''
if num >= 5:
    result = num * 2
else:
    result = num + 2
'''
print(result) #18

#3항 연산자
#형식) 변수 = 참 if(조건문) else 거짓

result = num*2 if num>=5 else num+2
print(result)


    
