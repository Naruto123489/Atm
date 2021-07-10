class atm:
    def __init__(self,CashWithdrawl,BalanceEnquiry,Accept_Card_Number,Accept_Pin_Number):
        self.Withdrawl=CashWithdrawl
        self.balance=BalanceEnquiry
        self.Card=Accept_Card_Number
        self.pin=Accept_Pin_Number
       

    def Withdrawl(self):
        print("Withdrawling cash")

    def balance(self):
        print("show balance enquiry")

    def Card(self):
        print("card number:")

    def pin(self):
        print("pin number: ")

Atm=atm(0,2500000000000,2054270756565086,4657)
print(Atm.Card)
print(Atm.balance)


    


        




        