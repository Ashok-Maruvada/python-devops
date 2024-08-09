sample_list=['k8','ansible','shell','jenkins']

# for i in sample_list:
#     print(i, len(i))

# # Print the element and its corresponding index
# for i,idx in enumerate(sample_list):
#     print(i,idx)

# Range based for loop
#sample_range= range(0, len(sample_list))
#print(sample_list, type(sample_range))

# for idx in range(0, len(sample_list)):
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx]=='shell':
#         continue
#     print(idx,sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx]=='shell':
#         break
#     print(idx,sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx]=='shell':
#         exit(1)
#     print(idx,sample_list[idx])

# for idx in range(0, len(sample_list)):
#     if sample_list[idx]=='shell':
#         pass
#     print(idx,sample_list[idx])

# print(sample_list)

# sample_list=['k8','ansible','shell','jenkins','Docker']
# idx=0

# while idx<len(sample_list):
#     if sample_list[idx]=='jenkins':
#         break
#     print(idx, sample_list[idx])
#     idx+=1

sample_dict = {1: 1, 2: 4, 3: 9}    

for i,j in sample_dict.items():
    print(i, j)