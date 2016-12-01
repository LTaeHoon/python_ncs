'''
MySQL DBMS = Maria DBMS

'''

import mysql.connector #db 연동에 필요한 모듈 추가
from mysql.connector import errorcode #db 연동 시 error 체크

#mysql/mariaDB 환경변수 설정
config ={
    'user':'scott',
    'password':'tiger',
    'host':'127.0.0.1',
    'database':'work',
    'port':'3306'
    }
try:
    #DB 연결 객체
    conn = mysql.connector.connect(**config)
    #SQL 실행 객체 생성
    cursor = conn.cursor()
    
    #레코드 추가
    ''' 
    sql = "insert into goods values(5,'테스트',5,400000)"
    cursor.execute(sql) #sql 실행
    conn.commit() #db 반영
    
    sql = "insert into goods values(%s, %s, %s, %s)"
    code = input('코드 입력 :')
    name = input('상품명 입력 :')
    su = input('수량 입력 :')
    dan = input('단가 입력 :')
    sql_data = (code,name,su,dan)
    cursor.execute(sql,sql_data)
    conn.commit() #db 반영
    '''
    
    #레코드 수정
    '''
    sql ="update goods set name = 'test' where code=5"
    cursor.execute(sql)
    conn.commit() #db반영
    '''
    '''
    sql = "update goods set name=%s where code = %s"
    code = input('수정할 코드 입력 :')
    name = input('수정할 상품명 입력 :')
    sql_data = (name,code)
    cursor.execute(sql,sql_data)
    conn.commit()
    '''
    
    #레코드 삭제
    '''
    del_code = input('삭제할 코드 입력 : ')
    sql ="delete from goods where code ="+del_code
    cursor.execute(sql)
    conn.commit()
    '''
    #goods 테이블 전체 목록 보기
    '''
    sql ="select * from goods"
    cursor.execute(sql) #sql문 실행
    '''
    #레코드 출력 : 양식문자 사용
    '''
    for r in cursor.fetchall():  #fetchone() 처음 검색된 레코드 하나만 사용
        #print(r) #tuple type 출력
        print('%d  %s  %d  %d'%r)
    '''
    #조건 검색 : 상품명
    '''
    name = input('조회할 상품명 입력 :')
    sql = "select * from goods where name = '{}'".format(name)
    cursor.execute(sql) #sql문 실행
    '''
    name = input('조회할 상품명 입력:')
    sql = "select * from goods where name like '%{}%'".format(name)   
    cursor.execute(sql) #sql문 실행
   
    #레코드 출력 : index 이용
    for row in cursor: 
        #print(row[0],row[1],row[2],row[3])
        print(str(row[0])+' '+row[1]+' '+str(row[2])+' '+str(row[3])) #숫자인 경우 문자열로 형변환 해줘야 다른 문자열과 결합이 가능함
        
# DB 연결 예외 처리          
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('id or password 오류')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('db 연동 오류')
    else:
        print('기타 에러:', err)
    conn.rollback() # 롤백 처리
finally:
    cursor.close(); conn.close() # 연결 객체 닫기 