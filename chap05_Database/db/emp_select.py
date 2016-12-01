'''
emp_select.py
 1. 전체 사원의 목록 검색
 2. 사원이름으로 조건 검색

'''

import mysql.connector #db 연동에 필요한 모듈 추가
from mysql.connector import errorcode #db 연동 시 error 체크


config ={
    'user':'scott',
    'password':'tiger',
    'host':'127.0.0.1',
    'database':'work',
    'port':'3306'
    }
    
try : 
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = "select * from emp"
        cursor.execute(sql)
        dataset=cursor.fetchall()

        for r in dataset:
            print(r[0], r[1], r[2], r[3], r[4], r[5])
        
        name=input('조회할 사원이름 입력 :')
        sql = "select * from emp where ename like '%{}%'".format(name)
        cursor.execute(sql)
        for r in cursor :     
            print(r[0], r[1], r[2], r[3], r[4], r[5])
             
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