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
    
    #1. url에서 data 요청
    
    url = "https://api.github.com/repos/pydata/pandas/milestones/28/labels"
    url2 = "http://192.168.0.145:8282/Data_Server/data/labels.json"
    result = requests.get(url2) #data 가져오기
    print(type(result))
    
    #2.json data 변환
    data=result.json()
    
    print(type(data))
    #3. json data 출력
    cnt=1

    for d in data:
        print('['+str(cnt)+']',d['id'],d['url'],d['name'],d['color'],d['default'])
        cnt+=1
        
    '''
    #4. table에 레코드 저장
    sql = "insert into labels values(%s, %s, %s, %s, %s, %s)"
    cnt = 1
    for d in data: 
        id = d['id'];url=d['url'];name=d['name'];color=d['color'];default=d['default']
        sql_data =(cnt,id,url,name,color,default)
        cursor.execute(sql,sql_data)
        conn.commit()
        cnt+=1
    
    #5. 테이블 전체 레코드 조회
    sql ="select * from labels"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for r in dataset:
        print(r)
    print('전체 레코드 수:%d'%len(dataset))
    ''' 
        
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