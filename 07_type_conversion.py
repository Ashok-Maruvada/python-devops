sample_str="this is a string"

sample_list=list(sample_str)
print(sample_list) # ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

sample_tuple=tuple(sample_str)
print(sample_tuple) # ('t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g')

# Accept input from a user
user_input=input()
print(user_input, type(user_input))