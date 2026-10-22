print("First Python Code!!!")

#Commenting(This line is also commented)

#Use the '#' Symbol for single line comments and " '''<your text>''' " syntax for multiline comments. (This line is also commented)
# Comments are used by the developer to state about the code. (This line is also commented)
# Comments are not executed when the program is running(This line is also commented)

#Ex:
#This is a single line comment!
'''This is a
multi-line comment!'''

#Varibales

#A variable is a container that holds a value of any type in Python. Syntactically no need of declaring a data type when defining a variable.

#Ex:

a = 2
b = 2.5
c = "Hello Python!"
d = True

#Data types
'''Data type defines the type of the value a varibale can hold
*int - Integer values
*float - Value with decimal points
*str - String(text) value
*bool - Boolean values (True, False)
Are the main primitive data types being dicussed in here
'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Strings
'''String values can be defined in three ways in Python.
In single quotes - ' '
In double quotes - " "
In triple quotes - ''' '''
*The beginning and the ending quotes must be in the same type.
*One type of quotes can be defined within a pair of quotes of another type or can be nested (Except in some speacial cases).
'''
#Ex:
word = 'Apple'
word2 = "Orange"
word3 = '''Papaya'''
#Nested quotes
word4 = '"Car"'
word5 = "'Bike'"
#ACTIVITY - Try other patternes of quote nesting yourself and check results by printing the values

#Type Casting
'''Type Casting is simply defining the data type of the variable.
The data type of the variable is declared on the run or, in other words, while the program is being executed
We can type cast into int, float, str, bool.
'''
#Ex:
d1 = float(a); print(d1)#output - 2.0
e = int(b); print(e)#output - 2
f = str(a); print(f)#output - 2
g = str(b); print(g)#output - 2.5
h = int(g); print(h)#output - ?.....
i = str(d); print(i)#output - ?.....

#Applying operators on variables
'''Addition(+), Multiplication (*), Substraction(-), division(/), mod(%), exponential(^) can be applied over numeric data types
Addition(+) and Multiplication (*) can be applied over string data type (str)'''

#Ex:
j = a*3; print(j) #Output - 6
k0 = b*3; print(k0) #Output - 7.5
k1 = c*3; print(k1) #Output - 
k = a + 1; print(k) #Adding integer to integer data type. Output - 3
l = b + 2.0; print(l) #Adding float to float data type. Output - 4.5
m = a + b; print(m) #Adding integer to float data type. Will output a float value. Output - 4.5 again
#ACTIVITY: Try other operators yourself (-,*,/,%)
n = c + 'I am a developer'; print(n) #Concatenating to strings. But it prints without spaces. Output - Hello Python!I am a developer
o = n + ' ' + 'I am a developer'; print(o) #Prnting with spaces. Output - Hello Python! I am a developer

#The escape character - \

'''The escape character tells the Python interpreter to treat the consequent character after it in a special manner.
It can be used to make effect on values by defining a special character (string) or to cancel the effect of a particular special character.

Ex:
*Try two lines of code below which are associated with the new line character and check the outputs. Understand what's happening.
'''
url = "C:\user\norman\photos"; print(url)
url2 = "C:\user\\norman\photos"; print(url)

'''Try this also (Uncomment the line of code)
worderr = ''''Oops!''''; print(worderr) #Just nested a single quote within a triple quote :)
'''
#Then try this and uderstand what has happened.
wordnoerr = '''\'Alright!\''''; print(wordnoerr)

#END OF DAY 01