# There are 2 methods to create a tuple
# 1. ()
# 2. tuple()
# Behavior: They're immutable

sample_tuple=('jira','ansible','k8','terraform','shell','jenkins')

element=sample_tuple[1]
print(element)

element=sample_tuple[-1]
print(element)

#slicing
sample_slice=sample_tuple[1:3]
print(sample_slice)

sliced_len=len(sample_slice)
print("length of sample slice:",sliced_len)

# Operations
res_tuple=sample_slice+sample_tuple
print(res_tuple)

res_tuple1=sample_slice*2
print(res_tuple1)

# Methods
res_index=sample_tuple.index('k8')
print(res_index)

# Tuple unpacking
ansible, terraform, jenkins, docker, k8s = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")
print(ansible, terraform, jenkins, docker, k8s)

