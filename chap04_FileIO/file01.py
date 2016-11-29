'''
파일 입출력(file input/output)
- 입출력 시(file, db) 반드시 예외 처리한다.
 형식) open('파일경로/파일명',mode ='r' or 'w' or 'a')
     mode = 'r' : 파일 읽기
     mode = 'w' : 파일 쓰기
     mode = 'a' : 파일 쓰기 + 추가
     
     #open 객체 닫기
     object.close()
     
'''
import os

try : 
    ''' 특정 경로의 파일 읽기
    test = open('C:/NCS/ftest1.txt',mode='r') # 1. file open
    print(test.read())# 2. file사용 : file 전체 읽고, 출력
    test.close() # 3. file 닫기
    '''
    
    #1. 현재 경로의 파일 읽기
    #print(os.getcwd()) # 현재 경로를 읽어오는 함수
    ftest1 = open(os.getcwd()+'/data/ftest1.txt',mode='r')
    print(ftest1.read()) #파일 전체 읽기
    ftest1.close()
    
    # 2. 파일 쓰기
    ftest2 = open(os.getcwd()+'/data/ftest2.txt',mode='w')
    ftest2.write('my first text~~~') #파일 쓰기
    ftest2.close() # 파일 닫기
    
    # 3. 파일 쓰기 (내용 추가)
    ftest3 = open(os.getcwd()+'/data/ftest2.txt',mode='a')
    ftest3.write('\nmy second text ~~~') #파일 쓰기(추가)
    ftest3.close()
    
    # 4. readline() : 줄 단위 읽기
    ftest4 = open(os.getcwd()+'/data/ftest2.txt',mode='r')
    f = ftest4.readlines() # 줄 단위 읽기
    print(f) #['my first text~~~\n', 'my second text ~~~']
    print(type(f)) #<class 'list'>
    ftest4.close()
    '''
    my first text~~~
    my second text ~~~
    '''
    #for 변수 in 자료구조 :
    for line in f : #'my first text~~~\n'
    #print(line)
        for l in line.split('\n'):  #my first text~~~ \n
            if l != '':
                print(l)
                
    #문)ftest1.txt 파일을 대상으로 줄단위 읽어서 공백없이 콘솔에 출력하시오.
    ftest5 =open(os.getcwd()+'/data/ftest1.txt',mode ='r')
    fline=ftest5.readlines();
    print(fline)
    print(type(fline))
    ftest5.close()
    
    #ftest1.txt 파일을 줄 단위로 읽어서 출력
    doc =[] #문단 저장 - 빈 list
    word = [] #단어 저장 - 빈 list
    for line in fline :
        for li in line.split('\n'):
            if li!='':
                print(li)
                doc.append(li) #문단 저장
                for w in li.split(' '):
                    word.append(w)
    
    print('문단 :',doc)
    print('문단 수 :',len(doc))
    print('단어 :',word)
    print('단어 수 :',len(word))

    '''
    object.read() : 전체 문서 읽기
    object.readline() : 한 줄 읽기
    object.readlines() : 줄 단위 전체 읽기
    '''
    #with문 이용 파일 출력
    #형식) with open('파일명',mode='r/w/a') as 객체명:
    with open(os.getcwd()+'/data/ftext3.txt',mode='w',encoding='utf-8') as f2 :
    #f2 = open()
        f2.write('파이썬 파일 작성 연습')
        f2.write('\n파이썬 파일 작성 연습2')
        #with 블럭 벗어나면 자동 close 됨
        #f2.close()
    with open(os.getcwd()+'/data/ftext3.txt',mode='r',encoding='utf-8') as f3 :
        print(f3.read())
        
except FileNotFoundError as e:
    print('Error 발생 :',e)




