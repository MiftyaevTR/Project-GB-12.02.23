
def sort_array (array):
    new_array=[]
    for el in array:
        if len(str(el))<=3:
            new_array.append(el)
    return new_array
    
array=['hello', '2', 'world', ':-)']
print(sort_array(array))