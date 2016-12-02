'''
Oracle DB 연동

'''

import cx_Oracle  #orcle 연동 모듈 추가

try :
    #db 연동 객체 생성
    dsn = cx_Oracle.makedsn("127.0.0.1", 1521, "orcl")
    conn = cx_Oracle.connect("scott", "tiger", dsn)
    #SQL 실행 객체 생성
    cursor=conn.cursor()
    
    #dept 테이블 전체 목록 조회
    sql ="select * from dept"
    cursor.execute(sql)
    
    for r in cursor.fetchall() :
        print(r[0],r[1],r[2])
    
except cx_Oracle.DatabaseError as e:
    print('Error 발생 :',e)