'''
우편번호 찾기 - 52,144개
135-806[Tab]서울[Tab]강남구[Tab]개포1동 경남아파트[Tab]1
[우편번호] [도/시] [구] [동~] [세부주소]
'''

import os

try:
    dong = input('동을 입력하세요:') #개포
    
    #우편번호 파일 읽기
    files = open(os.getcwd()+'/data/zipcode.txt',mode='r',encoding='utf-8')
    lines=files.readline() #첫번째 읽기
    #print(lines)
    while lines : #NULL 이면 반복 중지
        line = lines.split('\t') #tab키 단위로 토큰(단어) 생성
        #﻿135-806    서울    강남구    개포1동 경남아파트        1
        #line[0] line[1] line[2]  line[3]     line[4]
        if line[3].startswith(dong) :
            print('['+line[0]+']' + ' ' + line[1] +' '+line[2]+' '+line[3]+' '+line[4]) 
    
        lines=files.readline() # 두번째 읽기~
    
    #open 객체 닫기
    files.close()
except FileNotFoundError as e:
    print('Error 발생:',e)