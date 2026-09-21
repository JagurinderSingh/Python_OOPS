# also known as dunder method

# Magic methods are special methods and each magic method has superpower which is shown as __name__ - magic method e.g. __init__ constructor is also a magic method it has got a superpower, unlike other methods, the code inside it is directly triggered as soon as the object is created for the class.

# more magic_methods

class Temp:

  def __init__(self):
    print("Hello")

obj = Temp()

# Constructor helps us to actually write such code inside it which we want ourselves to handle, like the control will be entirely in our hand. 

# In big applications, we write specific configuration code inside it e.g. connecting to database, etc cause we can't rely on the user for such things while other things such as connecting to internet or database, etc