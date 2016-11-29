'''
교차검정 : 모델의 과적합 여부를 검정하는 방법

- 5겹 교차검정 예시
dataset = [1,2,3,4,5]
- 검정 데이터 : 1
- 훈련 데이터 : [2,3,4,5]
- 검정 데이터 : 2
- 훈련 데이터 : [1,3,4,5]
    :
- 검정 데이터 : 5
- 훈련 데이터 : [1,2,3,4]

'''

dataset = [1,2,3,4,5]
k=5
cnt =0
for i in range(k): #0~4
    test = dataset[i] #test=1
    train = dataset[i+1: ] #train=[2,3,4,5]
    if i>=1 and i<=3: 
        cnt+=1
        train.extend(dataset[i-cnt:i])
    else:
        train.extend(dataset[:i])
    print(test)
    print(train)
    