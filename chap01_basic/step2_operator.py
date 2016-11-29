'''
연산자
1. 변수에 값 할당
2. print 출력 양식
3. 산술, 관계, 논리 연산자
4. escape 문자 처리
'''

# 1. 변수에 값 할당(=)

v1 = v2 = v3 = 100
print(v1,v2,v3)

#동일 줄에 중복 출력
print('출력1',end=' ') #출력1,출력2
print('출력2')

v1, v2 = 100, 200
print(v1, v2)
#변수 교체
v2, v1 = v1,v2

print(v1, v2)

#패킹(packing) 할당
v1,*v2 = [1,2,3,4,5] #1 [2, 3, 4, 5]
print(v1,v2)

*v1,v2 = [1,2,3,4,5] #[1, 2, 3, 4] 5
print(v1,v2)

*v1,v2,v3 = [1,2,3,4,5]
print(v1,v2,v3) #[1, 2, 3] 4 5

#2.print 출력 양식

#1) format()
print(format(3.14159,'8.3f')) #   3.142
print(format(12345,"10d")) #     12345
print(format(12345,"3,d")) #12,345

#함수 도움말 보기
help(format)
#2) 양식문자
#형식) print('%양식문자' %(변수))

'''
%양식문자
%s : 문자열
%c : 한개 문자
%d : 정수
%f : 실수
%o : 8진수
%x : 16진수
%% : % 출력
'''

num1 = 10;num2 =20
tot = num1 + num2
print('10 + 20 = %d'%(tot)) # 10 + 20 = 30
print('%d + %d = %d'%(num1,num2,tot)) #10 + 20 = 30
print('이름은 %s이고, 나이는 %d 입니다.'%('홍길동',35))
# 이름은 홍길동이고, 나이는 35 입니다.

print('전체 %d%%가 170cm 이상이다.'%50) #외부에서 들어오는 변수가 한개인 경우 %() 괄호를 생략할 수 있음

#3) 외부 상수 입력
#형식) print('{}'.format(값))

print('이름은 {}이고, 나이는 {} 입니다.'.format('홍길동',35))
print('이름은 {0}이고, 나이는 {1} 입니다.'.format('홍길동',35))
print('이름은 {1}이고, 나이는 {0} 입니다.'.format(35,'홍길동'))

#3. 산술,관계,논리 연산자

print('산술연산자 :', 10+3, 10-3, 10*3, 10/3, 10//3, 10%3, 10**3)
print('관계연산자 :', 5>3, 5>=2,5!=4, 5==5)
print('논리연산자:', 5>4 and 5==3, 5>=3 or 5==6, not(5>3))

print('대한민국' + '우리나라') #결합연산자
print('='*50) #반복

#카운터 변수/누적 변수
cnt =0
cnt = cnt + 1 #카운터 변수
cnt += 1 #카운터 변수
print(cnt)

tot = 0
tot += cnt #누적변수 tot = tot(0) + cnt(2)
print(tot)

#4.escape 문자 처리 : 이탈문자 : 특수문자(',") or 특수기능(엔터키,탭)

print('\nescape 문자 처리')
print('\\n출력') #escape 기능 차단1
print(r'\n출력') #escape 기능 차단2

#C:\\Python34\\lib

# 문) c:\'aa'\"abc.txt"
print('c:\\\'aa\'\\\"abc.txt\"')

string = "우리나라 대한민국" # 한 줄 문자열
multiline = """안녕하세요
파이션에 오신걸 환영합니다.
파이션은 만능언어입니다.
반갑습니다.
"""
print(multiline)

query = """create table test(
id varchar(20) primary key,
name varchar(30) not null,
age int not null);
"""

print(query)

#키워드 입력

a = int(input("첫번째 숫자를 입력:")) #10 키보드 -> 정수
b= int(input("두번째 숫자 입력:")) #20
add = a+b
print('add = %d'%add)

#키보드 -> 실수
a = float(input("첫번째 숫자를 입력:")) #10
b= float(input("두번째 숫자 입력:")) #20
add = a+b
print('add = %.3f'%add)
