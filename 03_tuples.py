# There are 2 methods to create a tuple
# 1. ()
# 2. tuple()
# Behavior: They're immutable

sample_tuple=('jira','ansible','terraform','shell','jenkins')

element=sample_tuple[1]
print(element)

element=sample_tuple[-1]
print(element)

#slicing
sample_slice=sample_tuple[1:3]
print(sample_slice)

sliced_len=len(sample_slice)
print("length of sample slice:",sliced_len)