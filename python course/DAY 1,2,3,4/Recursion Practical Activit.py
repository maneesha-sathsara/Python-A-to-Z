'''
#Actiivty01
def count_down(n):
    if n==0:
        print("Finished")
    else:
        print(n)
        count_down(n-1)

count_down(3)




#modify:
def count_down (n):
    if n==0:
        print("Finished")
    else:
        print(n)
        count_down(n-1)

count_down(5)


#Activity02
def show_steps(n):
    if n<=1:
        print ("Base Case")
    else:
        print("step", n)
        show_steps(n-1)

show_steps(4)

'''

#Activity03
def trace (n):
    print("Entering", n)
    if n==0:
        print("Base")
    else:
        trace(n-1)
    print("Leaving", n)

trace(2)