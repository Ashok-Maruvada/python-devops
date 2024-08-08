# A Set returns unique elements that is stored inside that variable
# Sets don't consider the order of insertion
# Sets don't support indexing
sample_set={1,2,3,6,3,5}
print(sample_set)

# Add elements to a set
sample_set={1,2,3,6,3,5}
"""
sample_set[1]=10
print(sample_set)

Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/06_sets.py", line 9, in <module>
    sample_set[1]=10
TypeError: 'set' object does not support item assignment

"""
sample_set.add(4)
print(sample_set)

print(sample_set[2])
"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/06_sets.py", line 22, in <module>
    print(sample_set[2])
TypeError: 'set' object is not subscriptable
"""
# intersection(), union()