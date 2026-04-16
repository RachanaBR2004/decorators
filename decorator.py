
'''def fun(func):#decorator
    def say_bye():#wrapper
        func()
        print("bye")
    return say_bye

@fun
def say_hello():#original function
    print("hello")
say_hello()    
'''
'''
def fun(func):#decorator
    def say_bye():#wrapper
        func()
        print("bye")
    return say_bye


def say_hello():#original function
    print("hello")
my_fun=fun(say_hello)
my_fun()
'''

def take_test(func):
    def online_test():
        func()
        print("surprise test")
    return online_test

@take_test
def take_class():
    print("class is going on")
take_class

def decorator(func):
    def wrapper():
        print("hii")
        func()
    return wrapper

@decorator
def original():
    print("hello")
original()


  
def decorator(func):
    def wrapper():
        func()
        print("hii")
    return wrapper

@decorator
def original():
    print("hello")
original()

def payment_check(func):
    def wrapper(amount):
        if (amount>=100):
            print("payment successful")
            func(amount)
        else:
            print("insufficient")
    return wrapper
#amount=int(input("enter the amount"))

@payment_check
def place_order(amount):
    print("order placed successfully")
place_order(99)
            

def auth_decorator(func):
    def wrapper():
        user='ravi'
        pwd=1234
        if (user==user and pwd==pwd):
            print("auth is successful")
            func()
        else:
            print("authication not fornd")
    return wrapper
user=input("enter the user")
pwd=int(input("enter the pwd"))

@auth_decorator
def say_hello():
    print("new aut")
say_hello()

            

















