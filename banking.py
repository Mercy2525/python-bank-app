# Today's discussion
# Banking system using OOP
# has a function to show user details 
# child class : bank 
# stores details about the account balance 
# stores details about the amount 
# allos for deposits, withdraw, view balance
#parent class: User

#self is current instance of a class

class User:
    balance=10
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
      
    
    def show_user_details(self):
        print(f'Hello, {self.name}')
        print(f'Hello, {self.age} yrs')
        print(f'Hello, {self.gender}')
   

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.calc_balance(amount=2)
        self.withdraw(deduction=0)
       

    @classmethod
    def calc_balance(cls,amount):
        cls.balance+=amount
        return amount
        #return print(f' Current Balance: ${cls.balance}')
    
    @classmethod
    def withdraw(cls,deduction):
        cls.balance-=deduction
        #return print(f' Current Balance: ${cls.balance}')
    
    
    def display_banking_info(self):
        print(f'Hello, {self.name}, {self.amount}')
        pass



user1=Bank('Masibo',18, 'Male')
user1.calc_balance(3000)
user1.withdraw(200)
user1.display_banking_info()


















