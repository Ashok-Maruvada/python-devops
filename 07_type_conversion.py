sample_str="this is a string"

sample_list=list(sample_str)
print(sample_list) # ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

sample_tuple=tuple(sample_str)
print(sample_tuple) # ('t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g')

# Accept input from a user
user_input=input()
# whatever u enter whether number, string, it takes that as string
print(user_input, type(user_input))

user_input=input("enter anything: ")
print(user_input, type(user_input))
add_10=int(user_input)+10 
print(add_10, type(add_10))

split_input="10 100 20 30 40 50".split()
print(split_input)