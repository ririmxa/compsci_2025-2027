'''price = 10 # 'variable' = 'value' (integer = when a number doesn't have a decimal point)
price = 20 # python executes the code line by line, so now, the price is 20 not 10
print(price)
name = "Mosh" # this is a string
rating = 4.9 # this is float because of the decimal point
is_published = False # boolean, could also be True (remember that python is case sensitive so "false" wouldn't work)

######################

name = input("What is your name? ") # we're "calling" the function 'input'
print("Hi "+ name) 

name = input("What is your name? ")
color = input("What is your favourite color? ")
print(name + " likes " + color)

######################

birth_year = input("Birth year: ")
age  = 2019 - birth_year
print(age) # this won't work because we're mixing a string with a integer BIG NO!!, we have to convert it

birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print(age)

weight_pd = input("What's your weight (in pounds)? ")
end_weight = int(weight_pd) * 0.454
print(end_weight)

#######################

course = 'Python for Beginners'
another = course[:]
print(course[0]) # this will print 'P', because 0 = 1 in python
print(course[-1]) # this will print 's', because it prints the last character
print(course[0:3]) # this will print Pyt (it excludes '3')
print(course[0:]) # this will print the whole message
print(course[1:]) # this will print the whole message except 'P'
print(course[:5]) # this will print 'Pytho'
print(another) # this will print the whole message

name = "Jennifer"
print(name[1:-1]) #this will print 'ennife'

#######################

first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder" 
print(message) # this will do the trick for shorter code, but what about longer messages?

first = "John"
last = "Smith"
msg = f"{first} [{last}] is a coder" # this is a formatted string
print(msg)

#######################

course = "Python for Beginners"
print(len(course)) # len fuction is a general purpose function (it's not only used for counting the length, but in this case it is)
course.upper # when you write '.' it shows every possible function for strings
print(course.upper()) # upper cases the whole message
print(course.lower()) # lower cases the whole message
print(course.find("P")) # returns 0, because P's index is 0 (0=1!!)
print(course.find("Beginners")) # returns 11, because it's index is 11
print(course.replace("Beginners", "Absoluter Beginners")) # replaces the string (case sensitive!)
print("Python" in course) # we get True
print(course.title()) # upper cases every first letter of the word
'''
#######################

