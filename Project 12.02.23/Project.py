# Подробное описание работы данной программы в файле README

def sort_array (array):
    new_array=[]
    for el in array:
        if len(str(el))<=3:
            new_array.append(el)
    return new_array
    
# array=['hello', '2', 'world', ':-)']
# print(sort_array(array))

# array2=['1234', '1567', '-2', 'computer science']
# print(sort_array(array2))

array3=['Russian','Denmark', 'Kazan']
print(sort_array(array3))