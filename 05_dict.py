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

"""
sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
print(sample_dict[[1, 2, 3, 4]]) 

as list is mutable data type but dict-key is immutable. so its gives an error

Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/05_dict.py", line 16, in <module>
    sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
TypeError: unhashable type: 'list'
"""

sample_dict = {"1": 1, 2: 4, 3: 9,3: 14}
dict_keys=sample_dict.keys()
dict_values=sample_dict.values()
dict_items=sample_dict.items()
print(dict_keys,dict_values,dict_items)

# What happens if you access a key that is not present inside a dict
sample_dict = {1: 1, 2: 4, 3: 9}
print(sample_dict[4])