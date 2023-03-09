import math
# string data type

#literal assigment .....
first = "Rohit"
last ="Singh"

# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

# making string using a contructor .......
# pizza = str("pepporaoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))


# concatinate ...................

fullName= first + last;
print(fullName)

# casting a number to a string 
decade =str(1980)
print(type(decade))

statement = "i like rock " + decade+ ""

# multiple lines .........................
multiline='''
Hey kese ho bhai         


I was checking on






you;
'''

print(multiline)

# escaping special characters ..................
sentence = 'I\'m back at work\t hey \n where'
print(sentence)

# string methods .........
print(first)
print(first.lower())
print(first.upper())


# capitalise the first word of very letter
print(multiline.title())

print(multiline.replace("was","ok"))

print(len(multiline))

# remove white space 
print(len(multiline.strip()))

print('')

# build a menu 
title = "menu".upper()
print(title.center(20,"#"))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("chesseCake".ljust(16,".") + "$4".rjust(4))

print("")

# string index values ....
print(first[1])
print(first[-1])

# range 
print(first[1:-1])

# some methods 
print(first.startswith("R"))

# math 
print(math.pi)
print(math.sqrt(64))
print(math.ceil(10.81))
print(math.floor(11.615))


#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if u attempt to cast incorrect data 
