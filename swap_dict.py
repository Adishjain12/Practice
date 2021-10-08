#Swap keys and values
#You can easily swap the key,dictionary pairs in Python, with a one liner.

#dict = {value:key for key, value in dict.items()}

dict = {'a': 1, 'b': 2, 'c': 3}
print(dict)

dict = {value:key for key, value in dict.items()}
print(dict)

#This will output

#{'a': 1, 'c': 3, 'b': 2}
#{1: 'a', 2: 'b', 3: 'c'}
