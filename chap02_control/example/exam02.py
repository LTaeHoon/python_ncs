'''
과제1
'''
'''
multiline 변수를 대상으로 단어를 분리(공백 기준) 하고, 단어 수를 출력하시오.

multiline="""안녕하세오. Python 세계로 오신걸
환영합니다.
파이션은 비단뱀 처럼 매력적인 언어입니다.""“

<<화면 출력 예시>>
안녕하세오.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
전체 단어수 : 10

'''

multistr ="""안녕하세오.
Python 세계로 오신걸 환영합니다.
파이션은 비단뱀 처럼 매력적인 언어입니다."""

result =[]
word =[]

for d in multistr.split(sep='\n'):
    result.append(d)
    for w in d.split(sep=' '):
        word.append(w)
        print(w)
print("전체 단어수 : %d"%len(word))
