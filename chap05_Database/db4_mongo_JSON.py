'''
MongoDB + JSON
'''
import requests  #site에서 data 요청 모듈 추가
from pymongo import MongoClient #db 연동 모듈 추가

#mongod 인스턴스 생성
conn = MongoClient('127.0.0.1')

#db.collecttion.함수()



#1. url에서 data 요청

url = "https://api.github.com/repos/pydata/pandas/milestones/28/labels"
url2 = "http://192.168.0.145:8282/Data_Server/data/labels.json"
result = requests.get(url2) #data 가져오기

#2.json data 변환
data=result.json()


#3. json data 출력
cnt=1

for d in data:
    print('['+str(cnt)+']',d['id'],d['url'],d['name'],d['color'],d['default'])
    cnt+=1

'''
4. MongoDB에 json data 저장하기
조건1> db명 : test_db
조건2> collection 명 : labels
조건3> 저장 data : data 변수 대상 (document:30개)
'''
db = conn.test_db
labels = db.labels
for d in data:
    labels.insert(d)

#전체 문서 보기
result = labels.find()
for r in result:
    print(r)

#키순서로 출력하기
doc_all = labels.find()
cnt =0

for doc in doc_all:
    print('[',cnt,']',doc['id'],doc['name'],doc['url'],doc['color'],doc['default'])
    cnt +=1
#collection 제거
labels.drop()