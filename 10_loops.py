sample_list=['k8','ansible','shell','jenkins']

# for i in sample_list:
#     print(i, len(i))

# # Print the element and its corresponding index
# for i,idx in enumerate(sample_list):
#     print(i,idx)

# Range based for loop
sample_range= range(0, len(sample_list))
#print(sample_list, type(sample_range))

for idx in range(0, len(sample_list)):
    print(idx, sample_list[idx])
                    