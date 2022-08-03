unwant_chars = [';', ':', '!', "*", " "]
 
test_string = "R;up * S:fdc ! R;ing * Egg:s !"
 
print ("Original String : " + test_string)

for i in unwant_chars :
    test_string = test_string.replace(i, '')
 
print ("Final list is : " + str(test_string))