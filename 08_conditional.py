# Check whether the given number is greater than 10 or not

user_input=int(input("enter a number:"))

# if user_input>10:
#     print("given number is greater than 10")
# else:
#     print("given number is less than or equal to 10")

# Check whether the given number is equal to 10 or greater than 10 or less than 10 or something else

# Method 1: Nested if-else
if user_input>10:
    print("given number is greater than 10")
else:
    if user_input<10:
        print("given number is less than 10")
    else:
        print("given number is equal to 10")
