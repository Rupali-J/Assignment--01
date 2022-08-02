test_list = ['apple', 'umbrella', 'ice', 'authority']

print("The original list : " + str(test_list))

append_str = 'an'

pre_res = [append_str +' '+ j for j in test_list]

print("list after prefix addition : " + str(pre_res))
