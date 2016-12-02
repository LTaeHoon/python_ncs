'''
Created on 2016. 12. 2.

@author: acorn
'''
import pymongo
from pymongo import MongoClient #db 연동 모듈 추가


#mongod 인스턴스 생성
conn = MongoClient('localhost')

#db.collecttion.함수()

#데이터베이스 생성
db = conn.test_db
#컬렉션 생성
collect = db.collect #collect = conn.test_db.collect
#doc 생성 :{'key':'value'}
doc1 ={'empno':'10001','name':'hong','phone':'010-111-1111','age':35}
doc2 ={'empno':'10002','name':'lee','age':35}
doc3 ={'empno':'10003','name':'yoo','phone':'010-222-2222','age':25}

#collection에 문서 추가

collect.insert(doc1)
collect.insert(doc2)
collect.insert(doc3)

#문서 삭제 : db.collection.remove()
#collect.remove({'empno':'10002'})

#문서 수정 : db.collection.update()
'''
collect.update({'empno':'10001'},{'$set':{'name':'kim'}},True)
'''
#전체 문서 조회
result = collect.find()

#조회 문서 단위 출력
for r in result:
    print(r)

#조건 검색
print('조건검색')
result2 = collect.find({'age':{'$gte':30}})
for r in result2:
    print(r)

#컬렉션 제거
collect.drop()