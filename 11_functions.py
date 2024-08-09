# def sample_func():
#     print("this is sample function")
# #calling the function
# sample_func()

def add(num1, num2):
    res=num1+num2
    return res
# calling the function
#addition= add(1,2)
addition=add(num1=2,num2=3)
print(addition)


def add(num1,num2,num3=1):
    res=num1+num2+num3
    return res

# call the function
addition=add(2,3)
print(addition)