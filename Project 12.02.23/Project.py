

array=['hello', '2', 'world', ':-)']
new_array=[]
for el in array:
    if len(str(el))<=3:
        new_array.append(el)
        
print(new_array)