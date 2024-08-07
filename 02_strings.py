sample_str='this is my choice'
print(sample_str)

# How to access individual characters from a string
print(sample_str[3])

# Slicing
#2nd_index is treated as 2nd_index-1
print(sample_str[1:3])

sample=sample_str[:]
print(sample)

sample=sample_str[2:4]
print(sample)

sample=sample_str[::2]
print(sample)

sample=sample_str[1::2]
print(sample)

# Reverse a string
sample=sample_str[::-1]
print("reversing the string",sample)

# Length of a string
length_str=len(sample_str)
print("length of string",length_str)
