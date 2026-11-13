'''

#IN Class Assignment
#01
def temp_F(temp_C):
    return (temp_C * 9/5) + 32

print(temp_F(35))


#02
def apply_discount(price,discount_precentage):
    discount = price * discount_precentage
    final_price = price - discount
    
    if discount_precentage > 50/100:
        print(f"High discount")
    else:
        print(f"Low Discount")
    return final_price

print(apply_discount(500, 20))



#03
def format_book_info (title,author):
    title = title.title()
    author = title.title()
    return f'(title) by (author)'
    

print(format_book_info("BUSINESS SKILLS", "ELON MUSK")) 


'''

#Recursion
def count_down (n):
    if n==0:
        return 
    print(n)
    count_down(n-1)

count_down(10)
print("--------------------")
#From loop
for n in range (10,0,-1):
    print(n)