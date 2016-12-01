'''
JSON data 가져와서 DB 저장
1. requests 라이브러리 준비
2. labels 테이블 생성
'''
import requests  #site에서 data 요청 모듈 추가
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
    #DB 연결 객체
    conn = mysql.connector.connect(**config)
    #SQL 사용 객체
    cursor = conn.cursor()
    
    
    
#DB 연결 예외 처리
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