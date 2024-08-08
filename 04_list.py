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

sample_list[len(sample_list)+1]='ansible'
print(sample_list)