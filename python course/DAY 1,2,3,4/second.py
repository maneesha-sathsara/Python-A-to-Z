'''
x=10
print(x)


math_mark= int(input(f"Input your maths mark:"))
eng_mark= int(input(f"Input your english marks:"))
tot_mark=math_mark+eng_mark

#INPUT AND OUTPUT
stu_no = "PS/2022/132"
name = input(f"{stu_no},What is your name:")
#print("Hello", name)
#OR
print(f"Hello, {name} Your Total marks is {tot_mark}")


a=int(input("What is value of a:"))
b=int(input("What is value of b:"))

 
a_sq = a*a
b_sq = b*b
c_sq = a_sq+ b_sq
c = c_sq**0.5

print(f"value of c_sq: {c_sq}")
print(f"value of c: {c}")



a = int(input("Enter value of a:" ))
b = int(input("Enter value of b:" ))
c = int(input("Enter value of c:" ))

sqrte = int(b*b - 4*a*c)**0.5
minus_b = -b
two_a = 2*a

eq_01 = (minus_b + sqrte)/two_a
eq_02 = (minus_b - sqrte)/two_a

print(f"Value of output:{eq_01} or {eq_02}")


m = int(input("Enter the value of m:"))
c = 299792458
squre_c = c*c
E = m*squre_c
print(f"your value of Energy according to the mass: {E}") 



#Conditional Statement
#01(If)

age = 20
if age>= 18:
    print("You're eligible for vote")

    
#02(If elif)

mark = int(input("What is your value:"))
if mark>= 75:
    print("Distinction")

elif mark >= 50:
    print("Pass")



#03(All condtions)

mark = int(input("What is your value:"))
if mark>= 75:
    print("Distinction")

elif mark >= 50:
    print("Pass")

else:
    print("work hard")
    


#04(For Loop)

for i in range(1,5):
    print(f"Student ID: {i}")

#OR
#for variable_Name in range(startNO, Itteration):
   # print(f"Student ID: {i}")


for i in range(1,5,2):
    print(f"Student ID: {i}")


#Not using pre increment & post increment


for i in str("Maneesha_Sathsara"):
    print(f"Your name: {i}")

'''

#05 While loop
#while condition:
#code
#update_condition


i= 0
while i<=5:
    print(i)
    i+=1


password = "Maneesha"


while password <= 3:
    password1 =str(input("Enter your password"))
    if password1 in password == password1:
        print(f"Your password matched:")
    elif:
        print("Your password not matched")


