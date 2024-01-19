nums = [1, 2, 1]
my_dict = {}

for i in nums:
    if i not in my_dict:
        my_dict[i] = 1
    elif i in my_dict:
        my_dict[i] += 1

max_key = max(my_dict, key=my_dict.get)
print(max_key)
