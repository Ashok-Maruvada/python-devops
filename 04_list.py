# creating list
sample_list=['ansible','shell','terraform','git'] # list()

# Indexing, slicing
sample_ele=sample_list[1]
print(sample_ele)

sample_lt=sample_list[1:3]
print(sample_lt)

sample_ele=sample_list[len(sample_list)-1]
print(sample_ele)

# List is a mutable data type
# Once defined, it can be altered
sample_list[0]='k8'
print(sample_list)

sample_list[len(sample_list)-1]='ansible'
print(sample_list)

# Append element to the list
sample_list=['ansible','k8','terraform','git','shell']
sample_list.append('jenkins')  # inplace operation
print(sample_list)

# Append list within list
sample_list.append(sample_list)
print(len(sample_list)) #7

# extend
sample_list=[1,3,'sam',True]
sample_list.extend(sample_list)
print(sample_list) #[1, 3, 'sam', True, 1, 3, 'sam', True]

# membership operator: in, not in
is_element=2 in sample_list
print(is_element)