'''
문제) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오

[ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 가스레인지 5 450000
4 HDTV 3 1500000
전체 레코드 수 : 4

[ 상품별 총금액 ]
냉장고 상품의 총 금액은 1,700,000
세탁기 상품의 총 금액은 1,650,000
가스레인지 상품의 총 금액은 2,250,000
HDTV 상품의 총 금액은 4,500,000
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
    #DB 연결 객체
    conn = mysql.connector.connect(**config)
    #SQL 실행 객체
    cursor = conn.cursor()
    
    sql="select * from goods"
    cursor.execute(sql)
    cnt =0
    
    print('[ goods 테이블 현황 ]')
    for r in cursor.fetchall() :
        print('%d  %s  %d  %d'%r)
        cnt +=1
    print('전체 레코드 수 :',cnt)
    
    cursor.execute('select name,su,dan from goods') 
    print('[ 상품별 총 금액 ]')
    for row in cursor:
        print(row[0]+' 상품의 총 금액은 '+ str(row[1]*row[2]))
           
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
