from collections import Counter
  
def unique(list1):
    print(*Counter(list1))

list1 = [10, 20, 10, 30, 40, 40, 50]
print("the unique values from 1st list is")
unique(list1)