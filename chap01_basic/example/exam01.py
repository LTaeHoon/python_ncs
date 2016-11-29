'''
step1, step2에 관련된 문제
'''

#문)다음 사다리꼴을 보고 넓이를 구하시오.
#조건1)데이터는 키보드 입력
#조건2)소수점 3자리 까지 출력
#조건3)사다리꼴 넓이 = (밑변 + 윗변)*높이 /2

#밑변 = 12, 윗변 = 7, 높이 = 9

#1. 키보드 입력
down = float(input('밑변 입력:'))
top = float(input('윗변 입력:'))
height = float(input('높이 입력:'))
#2. 연산
trape_area = (down + top)*height/2
#3. 출력
print('사다리꼴 넓이 = %.3f'%trape_area)

