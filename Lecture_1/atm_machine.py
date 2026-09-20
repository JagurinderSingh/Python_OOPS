#to name a class, use Pascal Case, meaning the first letter of each word is capitalized. e.g. AtmMachine, BankAccount, etc.

class Atm:

  # constructor - A function inside the class - when you have to create the variables inside the class, you have to use constructors and use self.

  # constructors - It is a special function, whatever is inside it, you don't need to call it explicitly, instead whatever is inside the constructor gets executed

  def __init__(self):
    self.pin = "" #two variables
    self.balance = 0
    self.menu()

  def menu(self):

    user_input = input("""
Hi, How can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit
>>> """)

    if user_input == "1":
      #create pin
      self.create_pin()

    elif user_input == "2":
      #change pin
      self.change_pin()

    elif user_input == "3":
      #check balance
      pass

    elif user_input == "4":
      #withdraw
      pass
    
    else:
      exit()

  def create_pin(self):
    user_pin = input("Enter your pin: ")
    self.pin = user_pin

    user_balance = int(input("Enter Balance: "))
    self.balance = user_balance

    print("Pin created successfully!")
    self.menu()

  def change_pin(self):
    old_pin = input("Enter Old Pin: ")

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input("Enter New Pin: ")
      self.pin = new_pin
      print("Pin change successfully!")
      self.menu()

    else:
      print("Nahi karne de sakta baba")
      self.menu()

obj = Atm() # Creating an object of Atm class


#print(type(obj))
# obj2 = Atm()
# print(obj2)

# There are two types of classes in the Python - Built in classes and User Defined Classes
