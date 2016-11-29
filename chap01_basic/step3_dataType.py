'''
자료형(data type)
1. python의 자료형
2. 문자열
3. python 기본 자료구조
'''

#1.python의 자료형

print(10, type(10)) #10 <class 'int'>
print(12.3045, type(12.3045)) #12.3045 <class 'float'>
print(True, type(False)) #True <class 'bool'>
a = 100; b=200
print(a>b) #False
print('abcd',type('abcd')) #abcd <class 'str'>

#2,8,16
print('\n진법변환')
print(10,bin(10),oct(10),hex(10)) #10->다른진법(0b1010 0o12 0xa)
print(10, 0b1010, 0o12, 0xa) #다른진법 -> 10진법로 변환

#2. 문자열 처리
'''
문자열 객체 처리
 - 문자열(string) : 문자들의 집합
 - 순서 있음
 - 수정불가(상수) : 문자열 수정 -> 새로운 객체 생성 
 - indexing 이용, slicing 가능
'''
st = '우리나라 대한민국 나의 조국은 대한민국 입니다.'
print(st, type(st)) # <class 'str'>
print('st 길이:',len(st))
print('국 글자 수 :', st.count('국')) #국 글자 수 : 3

#시작 문자 유무 리턴 -> True, False
print(st.startswith('우리'))
print(st.startswith('일본'))

#문자열 수정 -> new object
st2 ='홍길동' 
print('st2 주소:', id(st2)) #address 리턴  st2 주소: 39986320
st2 = '강호동' #수정
print('st2 주소:', id(st2)) #st2 주소: 39986640

#indexing = 색인[n]
result = st2[0] #첫번째 문자
print(result)
print('result:%c'%result)

result = st2[1:3] #1~2까지 문자열 저장
print('result:',result)

result = st2[:3] #0,1,2
print('result:',result)

result = st2[-1] #오른쪽 마지막
print('result:',result)

#문자열 분리 (split)
st3 = '나는 홍길동 입니다. 나이는 23세 이고, 주소는 서울 입니다.'
st4 = st3.split(sep=" ")
print('st4 :',st4) #st4 : ['나는', '홍길동', '입니다.', '나이는', '23세', '이고,', '주소는', '서울', '입니다.']

#문자열 결합 (join)
st5 = ' '.join(st4)
print('st5 :',st5) #st5 : 나는 홍길동 입니다. 나이는 23세 이고, 주소는 서울 입니다.

#3. python 기본 자료구조
# - memory 구조를 의미함

''' 
주요 자료구조
 - list : 1차원, index 사용(순서 존재)
 - tuple : 1차원, index 사용, 수정 불가능
 - set : 순서 없음, 중복 불가능
 - dict : key : value
 - data.frame : 별도의 패키지 필요함

'''

#1) list 구조
li = ['a','b','c']
print(li,li[:2]) #['a', 'b', 'c'] ['a', 'b']

# 원소 추가
li.append('d')
li[0] = 'aa' #수정
print(li) #['a', 'b', 'c', 'd']

#2) tuple 구조
t = (1,2,3,4)
print(t,t[:3]) #(1, 2, 3, 4) (1, 2, 3)

'''
t[3] = 44 # Error(수정 불가)
'''

#3) set 구조
s = {1,2,3,4,5}
print(s, type(s)) #{1, 2, 3, 4, 5} <class 'set'>
'''
result = s[3] #Error(index 사용 불가)
'''

#4) dict 구조
#형식) key:value -> json

d = {'name':'홍길동','age':35, 'addr':'서울시'}
print(d,type(d)) #순서는 random
#{'addr': '서울시', 'name': '홍길동', 'age': 35} <class 'dict'>

#key 로 접근
result =d['name']
print(result) # 홍길동

'''
result = d['홍길동']
result = d[0]
print(result)
'''













