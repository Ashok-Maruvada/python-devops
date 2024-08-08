#dictionary is like a key-value pair
#dict is mutable data type but keys are immutable
sample_dict= {1:1,2:4,3:9}
print(sample_dict)
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
print(sample_dict[3]) # gives latest value i.e 15

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict["1"])

sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
print(sample_dict[[1, 2, 3, 4]])