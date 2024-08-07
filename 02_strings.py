sample_str='this is my choice'
print(sample_str)

# How to access individual characters from a string
# space between the words is also considered in strings
# Python is based on Zero indexing i.e starts frrom zero index
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
print("reversing the string:",sample)

# Length of a string
length_str=len(sample_str)
print("length of string",length_str)

# Method
sample="heee"
print(sample.capitalize()) # "Heee"

# split(), join(), format(), count(), strip(), lstrip(), rstrip()

sample="this is my life"
split_str=sample.split() #output is a list
print(split_str, type(split_str))

join_str=' '.join(split_str)
print(join_str, type(join_str))

count_i=sample.count('i')
print(count_i)

sample='   this is my life    '
sample_str=sample.strip()
print(sample_str)

# Strings are immutable
sample="this is my life"
sample[0]='T'
print(sample)