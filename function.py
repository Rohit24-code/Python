# def :- is short for define 

#i am giving default value to argument as world



# i am using main function so that we can use hello function writing below also 

def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()


