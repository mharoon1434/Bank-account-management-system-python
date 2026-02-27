class bankAccount:
    def __init__(self,acc,pasword):
        self.Account_no=acc
        self.pasword=pasword
        self.balance=0
    def deposit(self,balance):
        self.balance+=balance
    def withDraw(self, Amount):
        if balance<Amount:
            print("Increase your balance! Your balance is {self.balance}")
        else:
            balance-=Amount
            print(f"{Amount} withdraw for your account ")
    def checkBalance(self):
        print(f"Your are balance is {self.balance}")
        if(self.balance==0):
            print("Increase your balance")
    @classmethod
    def checkInfo(cls,Account1):
        acc=str(input("Enter your account Number "))
        password=str(input("Enter your password "))
        for el in Account1:
            if el.Account_no==acc and el.pasword==password:
                return el
            else:
                return -1
def print_Further(el,Account1):
    print("Now your are in main Manu")
    print("1- for deposite money \n2- for withdraw \n3- for checkBalance\n")
    num=int(input("Your choice "))
    if num==1:
        Amo=int(input("Enter the money your deposite "))
        el.deposit(Amo)
        Again_Main(el,Account1)
    elif(num==2):
        Amo=int(input("Enter the money your withdraw "))
        el.withDraw(Amo)
        Again_Main(el,Account1)
    elif(num==3):
        el.checkBalance()
        Again_Main(el,Account1)
    else:
        return
def Again_Main(el,Account1):
    print("1- for going to back \n0- for return ")
    num=int(input("Your Choice "))
    if(num==1):
        print_Further(el,Account1) 
    if(num==0):
        main(Account1)
    else:
        Again_Main(el,Account1)

def main(Account1): 
    print("Hi login or sign up your account in HBL bank ")
    print('1- login \n2- sign up')
    num=int(input("Your Choice "))
    if(num==1):
        el=bankAccount.checkInfo(Account1)
        if(el!=-1):
            print_Further(el,Account1)
        else:
            print("Not correct information ")
            main(Account1)

    elif(num==2):
        ac="HBL-123"
        last=str(input("Enter the last character "))
        ac+=last
        password=str(input("Enter your password "))
        New_Account=bankAccount(ac,password)
        Account1.insert(0,New_Account)
        print('\n\n\nNow login to your account')
        el=bankAccount.checkInfo(Account1)
        if(el!=-1):
            print_Further(el,Account1)
        else:
            print("Not correct information ")
            main(Account1)
    else:
        print("Retry")

Account1=[bankAccount("HBL-123", "haroon123")]
  
main(Account1)