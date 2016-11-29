'''
문) 중첩함수를 적용하여 은행계좌 함수를 정의하시오.
<조건1> outer 함수 : bank_account() -> balance(잔액) 초기화, Inner함수 포함
<조건2> inner 함수 : getBalance() -> 잔액보기 : balance 출력
deposit() -> 입금하기 : balance += money
withdraw() -> 출금하기 : balance -= money
<조건4> 예외처리 : 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.’ 메시지 출력
<조건3> 기타 나머지는 출력 예시 참조
'''
'''
최초 계좌의 잔액을 입력하세요 : 1000
현재 계좌 잔액은 1000원 입니다.
입금액을 입력하세요 : 10000
10000원 입금 후 잔액은 11000원 입니다.
출금액을 입력하세요 : 8000
8000원 출금 후 잔액은 3000원 입니다.
'''


def bank_account(value):
    balance = value
    def getBalance():
        nonlocal balance
        return balance
        #print('잔액보기:', balance)
    def deposit(money):
        nonlocal balance
        balance += money
        return balance
    def withdraw(money):
        nonlocal balance
        balance -= money
        return balance
    return getBalance,deposit,withdraw

    
bal =int(input('최초 잔액을 입력하세요:'))
getbal, dep, wd = bank_account(bal)    
print('현재 계좌 잔액은 %d원 입니다.'%getbal())
inmon = int(input('입금액을 입력하세요:'))
print('%d원 입금 후 잔액은 %d원 입니다.'%(inmon,dep(inmon)))
outmon = int(input('츨금액을 입력하세요:'))
if outmon > getbal():
    print('잔액이 부족합니다.')
else:
    print('%d원 출금 후 잔액은 %d원 입니다.'%(outmon,wd(outmon)))
