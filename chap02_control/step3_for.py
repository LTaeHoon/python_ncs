'''
반복문(for)

형식) 
for  변수 in 자료구조 :
    실행문
    실행문
자료구조 : list, tuple, set, dict    
'''

# list 이용 
dataset = [1,2,3,4,5]

for d in dataset :
    print('원소 : ', d)
    
dataset2 = ['one', 'two', 'three']

for d2 in dataset2 :
    print(d2)    
    
# list -> list2 추가 
li1 = [1,2,3,4]
li2 = [] # 빈 list

for l in li1 :
    li2.append(l) 

print(li2) # [1, 2, 3, 4]   

# 문1) list1에 7개 원소가 있는데 그중 5이상만 list2에 넣으시오.
list1 = [2, 5, 7, 56, 54, 2, 6]
list2 = [] 

for li in list1 :
    if li >= 5 :
        list2.append(li)    
print(list2) # [5, 7, 56, 54, 6]
list2.sort() # 원소 오름차순 정렬 
print(list2) # [5, 6, 7, 54, 56]   
    
# tuple 이용 
t = (1,2,3)
for d in t :
    print(d, end = ' ') # 1 2 3 

print()
    
# set 이용 
s = {1,2,3,4,5}
for d in s :
    print(d, end = ' ')  # 1 2 3 4 5  

print()

# dict 이용 
d = {'name': '홍길동', 'age':'35', 'gender' : '남'}
for i in d.keys() : # d = d.keys()
    print(i, '->', d[i]) # key -> value
      

# 다중 for문 
'''
for i in d1 :
   for j in d2 :
      실행문
'''

l1 = [3, 4, 5]
l2 = [0.5, 0.25, 0.125] # 1/2, 1/4, 1/8

for i in l1 : # 3, 4, 5
    for j in l2 : # 0.5, 0.25, 0.125
        calc = i * j 
        print(calc, end = ' ')

print()

# 구구단 출력(2,3)
for i in [2,3,5,8] :
    # 바깥쪽 영역 
    print('~~~ {}단 ~~~'.format(i))
    for j in [1,2,3,4,5,6,7,8,9] :
        # 안쪽 영역 
        print('%d * %d = %d'%(i, j, i*j))
        
string = """나는 홍길동 입니다.
 나이는 23세 입니다.
 주소는 서울 입니다."""   
 
result = []
word = []
for doc in string.split('\n') : # 문장 
    result.append(doc) # 줄 단위
    for w in  doc.split(' ') :
        word.append(w)
    
print(result) # ['나는 홍길동 입니다.', ' 나이는 23세 입니다.', ' 주소는 서울 입니다.']   
print(word) # ['나는', '홍길동', '입니다.', '', '나이는', '23세', '입니다.', '', '주소는', '서울', '입니다.']     
print('단어 수 : ', len(word)) # 단어 수 :  11

''''
range(n,m) : n ~ m 정수 반환 
'''

r1 = range(10)
print(r1) # range(0, 10)
for d in r1 :
    print(d, end = ' ') # 0 1 2 3 4 5 6 7 8 9

r2 = range(1, 11) # 1 ~ 10    

for i in range(2, 10) : 
    # 바깥쪽 영역 
    print('~~~ {}단 ~~~'.format(i))
    for j in range(1, 10) :
        # 안쪽 영역 
        print('%d * %d = %d'%(i, j, i*j))




