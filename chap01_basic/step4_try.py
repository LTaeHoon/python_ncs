'''
예외처리 : run time error 발생 시 처리

try:
    예외발생 코드
except:
    예외처리 코드
finally:
    항상 실행 코드
'''

'''
print('프로그램 시작')

try:
    a = int(input('숫자입력:'))
    print('a:',a)
except :
    print('숫자 입력을 잘못했습니다.')

print('프로그램 종료')
'''

#2. 다양한 예외 처리 : 산술적 예외, type 오류, 파일 오류

import locale # 다국어 처리 모듈
locale.setlocale(locale.LC_ALL,locale='') #다국어 설정
print(locale.getlocale()) #('Korean_Korea', '949') #다국어 확인

print('프로그램 시작')
try:
    div = 10000 /2 
    #천단위 컴마
    fdiv = locale.format('%d',div,True)
    print('나눗셈 결과 {}이다.'.format(fdiv))
    a= int(input('숫자 입력:'))
    #div2 = 1000/0  #산술적 예외
    #print('div2:',div2)
    #f = open('c:\\test.txt') #파일 열기
except ZeroDivisionError as e:
    print('오류 발생')
    print('오류 정보 :',e)
except FileNotFoundError as e2:
    print('오류 정보:',e2)
except Exception as e3: #모든 예외 처리 클래스
    print('오류 정보:',e3)
finally:
    print('여기는 항상 실행됨')
print('프로그램 종료')