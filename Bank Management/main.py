import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists!")

    except Exception as err:
        print(f"An exception occurred as {err}")

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k =3)
        num = random.choices(string.digits, k = 6)
        spchar = random.choices("!@#$%&*",k=1)
        id = alpha+num+spchar
        random.shuffle(id)
        return "".join(id)


    #1
    def CreateAccount(self):
        info = {
            "name": input("Write your Name : "),
            "age": int(input("Age: ")),
            "email": input("Email : "),
            "pin": int(input("Create 4 Digit pin : ")),
            "account_number": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you are not eligible!")

        else:
            print("Account has been created successfully!")

        for i in info:
                print(f"{i} : {info[i]}")

        print("Please note down your account number")

        Bank.data.append(info)

        Bank.update()

    #2
    def Deposit(self):
     accnumber = input("Enter your account number : ")
     pin = int(input("Enter your pin : "))
    
     userdata = [
         i for i in Bank.data 
         if i['account_number']==accnumber and i['pin']==pin]
     
    #  print(userdata)

     if not userdata:
         print("Sorry No Data Found")

     else:
        amount = int(input("Enter Amount to deposite : "))
        if amount <= 0 :
            print("Enter a valid amount to deposite")
        else:
            userdata[0]['balance']+= amount
            Bank.update()
            print("Amount Deposited Successfully!")

    # 3
    def Withdraw(self):
     accnumber = input("Enter your account number : ")
     pin = int(input("Enter your pin : "))
    
     userdata = [
         i for i in Bank.data 
         if i['account_number']==accnumber and i['pin']==pin]

     if not userdata:
         print("Sorry No Data Found")

     else:
        amount = int(input("Enter Amount to withdraw : "))
        if amount <= 0 or amount > userdata[0]['balance']:
            print("Sorry, Something wrong try Again!")
        else:
            userdata[0]['balance']-= amount
            Bank.update()
            print("Amount withdrawn Successfully!")

    #4
    def ShowDetails(self):
         accnumber = input("Enter your account number : ")
         pin = int(input("Enter your pin : "))

         userdata = [
             i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin
         ]
         if not userdata:
            print('sorry invalid user!')
         print("-----Your information-----")
         for i in userdata[0]:
             print(f"{i} : {userdata[0][i]}")

         print("-----THANK YOU-----")




print("Press 1 for Create an Account")
print("Press 2 for Deposit Money in Bank")
print("Press 3 for Withdrawing Money")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Delete Account")

check = int(input("Tell Your Response :- "))

user = Bank()

if check == 1:
    user.CreateAccount()
if check == 2:
    user.Deposit()
if check == 3:
    user.Withdraw()
if check == 4:
    user.ShowDetails()
if check == 5:
    user.UpdateDetails()
if check == 6:
    user.Delete()