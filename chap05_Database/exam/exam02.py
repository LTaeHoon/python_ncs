'''
Created on 2016. 12. 1.

@author: acorn
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

while True:
    print('\t[레코드 처리 메뉴]')
    print('1.레코드 조회')
    print('2.레코드 추가')
    print('3.레코드 수정')
    print('4.레코드 삭제')
    print('5.프로그램 종료')
    
    menu = int(input('=> 메뉴번호 입력: '))
    if menu ==1:
        # 1. 레코드 조회
        print('레코드 조회!')
        try :
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            name=input('상품명 입력 :')
            if name!='':
                sql="select * from goods where name like '%{}%'".format(name)
                cursor.execute(sql)
                dataset=cursor.fetchall()
                for r in dataset:
                    print('%d %s %d %d'%r)
            else :
                print('상품명을 입력하세요')        
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
    elif menu==2:
        # 2. 레코드 추가
        print('레코드 추가!')
        try :
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = "insert into goods values(%s, %s, %s, %s)"
            code = input('코드 입력 :')
            name = input('상품명 입력 :')
            su = input('수량 입력 :')
            dan = input('단가 입력 :')
            sql_data = (code,name,su,dan)
            cursor.execute(sql,sql_data)
            conn.commit() #db 반영
            print('레코드 입력 완료')        
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
        
    elif menu==3:
        # 3. 레코드 수정
        print('레코드 수정')
        try :
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = "update goods set name=%s where code = %s"
            code = input('수정할 코드 입력 :')
            name = input('수정할 상품명 입력 :')
            sql_data = (name,code)
            cursor.execute(sql,sql_data)
            conn.commit() #db 반영
            print('레코드 수정 완료')        
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
    elif menu==4:
        # 4. 레코드 삭제
        print('레코드 삭제')
        try :
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            del_code = input('삭제할 코드 입력 : ')
            sql ="delete from goods where code ="+del_code
            cursor.execute(sql)
            conn.commit() #db 반영
            print('레코드 삭제 완료')        
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
       
    elif menu==5:
        print('프로그램 종료')
        break