def open_account() : 
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money) : 
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.")
    return balance + money

def withdraw(balance, money) :
    if balance >= money:
        print(f"출금 완료. 잔액은  {balance-money}원입니다.")
        return balance - money
    else :
        print (f"출금 안 됩니다. 잔액은 {balance}입니다")
        return balance
def withdraw_ataight (balance, money) :
    commission = 100
    return commission, balance- money - commission


balance = 0 
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_ataight(balance, 500)
print(f"수수료는 {commission}, 잔액은 {balance}입니다.")