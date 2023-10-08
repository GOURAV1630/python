class BankAccount:
    balance=0
    def deposit(self):
        a = int(input('Amount to be deposited:- '))
        self.balance += a
        print(f'Balance = Rs. {self.balance}')

    def withdraw(self):
        b = int(input('Enter amount to withdraw:- '))
        if b > self.balance:
            print(f'You do not have sufficient balance.\nCurrent Balance = Rs. {self.balance}')
        else:
            new_balance = self.balance - b
            self.balance = new_balance
            print(f'You current balance= Rs. {self.balance}')
    
    def check_balance(self):
        self.current = self.balance
        print(f'Balance = Rs.{self.current}')

account = BankAccount()

while True: 
    print('1. Deposit in your account')
    print('2. Withdraw amount from savings')
    print('3. Check Balance')
    print('4. Exit')
    choice = int(input('Enter your Choice(1,2,3,4) = '))
    if choice==1:
        account.deposit()
    elif choice==2:
        account.withdraw()
    elif choice==3:
        account.check_balance()
    elif choice==4:
        break
    else:
        print('Enter valid choice.')