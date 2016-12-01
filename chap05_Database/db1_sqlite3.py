'''
sqlite3 - 내장 DBMS (Database Management System) 
'''
#파이썬은 내장 DB로 sqlite3를 갖고 있음

import sqlite3

#sqlite3 버전 확인
print(sqlite3.sqlite_version_info) #(3, 8, 11)

# db 연동 객체 생성
conn = sqlite3.connect('nice.db') #nice.db 생성 + 연동 객체 생성(conn)
#SQL문 실행 객체 생성
cursor = conn.cursor()

#테이블 삭제
cursor.execute('drop table if exists test') # test 테이블 있으면 삭제
conn.commit() #db 반영

#테이블 생성
cursor.execute('create table test(name text(10),phone text(15),addr text(50))')

#레코드 추가
cursor.execute("insert into test values('홍길동','010-111-1111','서울시')") #따옴표 안에 같은 따옴표가 있으면 에러가 남. 따라서 홑, 쌍따옴표를 사용
cursor.execute("insert into test values('이순신','010-222-1111','남해시')")
cursor.execute("insert into test values('강감찬','010-333-1111','평양시')")
conn.commit() #db 반영

#레코드 조회/출력
cursor.execute('select * from test')
#cursor 객체를 이용하여 조회 결과를 출력
for r in cursor.fetchall():
    print(r) #tuple type으로 출력

#칼럼 단위 출력
cursor.execute('select * from test')
print('이름\t전화번호\t\t주소') #칼럼 제목 출력
for row in cursor :
    print(row[0] + '\t'+row[1]+'\t'+row[2])

#open 객체 닫기 : 순서는 역순
cursor.close()
conn.close()


