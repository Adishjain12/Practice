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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Python Program to Swap dictionary item’s position

# initializing dictionary
test_dict = {'Gfg': 4, 'is': 1, 'best': 8, 'for': 10, 'geeks': 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing swap indices
i, j = 1, 3

# conversion to tuples
tups = list(test_dict.items())

# swapping by indices
tups[i], tups[j] = tups[j], tups[i]

# converting back
res = dict(tups)

# printing result
print("The swapped dictionary : " + str(res))

