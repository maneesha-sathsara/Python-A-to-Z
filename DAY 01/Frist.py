"""

#single line comment

**************************************************
#Variables

#Introduction to variables
No need to declare type explicitly

Valid:
• age, user_name, price1

Invalid:
• 1age, user name, class

**************************************************
#Value Assignment methods

• single assignment;  x=10
• chained assignment;  x=y=z=10
• multiple assignment;  x,y,z=10,20,30
(variable can be reassined at any time)

**************************************************
Garbage Collection in Python

• Python automatically manages memory.
– When objects are no longer referenced, memory is freed.
– No manual memory allocation required.
– Helps prevent memory leaks in beginner programs.

**************************************************
Basic Data Types

Every value in Python has a data type.
- int → 10
- float → 19.99
- str → 'Hello'
- bool → True / False
- Use 'type(variable)' to check data type.

**************************************************

Type Casting (Converting data types)
 - Implicit Type Casting (Type Conversion)
     • Example: 5 + 2.5 → 7.5 (float)

- Explicit Type Casting (Type Conversion)
     • Example: int('10') → 10

**************************************************

Basic Operators in Python
• Arithmetic: +, -, *, /, %, //, **
• Assignment: =, +=, -=, *=
• Comparison: ==, !=, >, <, >=, <=

- Example:
➢ a = 10, b = 3
➢ a + b → 13
➢ a > b → True

**************************************************

Basic Input & Output

• print() displays output to the screen.
• input() collects user input as text.

- Example:
➢ name = input("Enter your name here:")
➢ print('Hello', name)
[Input() always return string]


**************************************************

Integrated Example Program:-

name = input('Enter your name here:')
age = int(input('Enter your age here:'))
print('Welcome', name)
print('Next year you will age:', age+1)


"""
