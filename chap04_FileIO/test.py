'''
평균, 분산, 표준편차 함수

'''
from math import sqrt

#평균 함수
def avg_function(x):
    tot = sum(x) #합계
    length = len(x) #길이
    avg = tot/length
    return avg

#list 자료
x =[5,9,1,7,4,6]

#평균 함수 호출
result = avg_function(x)
print('avg =',round(result,2))

#분산/표준편차
def var_sd_func(x):
    avg = avg_function(x)
    diff = [(xx-avg)**2 for xx in x] #차
    var = sum(diff)/(len(x)-1)
    sd = sqrt(var)
    print('var =',round(var,2))
    print('sd =',round(sd,2))

#분산/표준편차 함수 호출    
var_sd_func(x)

