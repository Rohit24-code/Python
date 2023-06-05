# def :- is short for define 

#i am giving default value to argument as world

def hello(to="world"):
    print("hello,", to)

name = input("what's your name? ")
hello(name)
