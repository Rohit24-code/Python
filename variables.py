            #------------string-and-input---------------#

# Ask user for their name 
name=input ("What is your name , ")


# Removes white space from string 
name=name.strip()

# Capitalise the first letter of each word
name=name.title()

# SPlititning a string  into sub string
first,last = name.split(" ")

# Say hello to user 
# print("my name is", name)

# we can also do this using 
# print("my name is",end="")
# print(name)

# we can also do this using 
print(f"my name is {first}")

# like we have end we have sep to as arguments 

# i can do all this on two lines 
# name=input ("What is your name , ").strip().title()   then we can print 




