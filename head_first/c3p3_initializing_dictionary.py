# though dictionaries are dynamic but we can't just try to update the
# value of the key that doesn't exists (has not been initialized)

# empty dictionary
fruits = {}
fruits['apples'] = 10

# trying to update value of the non-existent key, throws KeyError: 'bananas'
# fruits['bananas'] +=1

# to sort out we can use 'in' membership, check if bananas are already in the dictionary,
# if yes then increment
# if no then initialize for the first time
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

print(fruits)

# we can also try to solve this by using 'not in' membership above
if 'oranges' not in fruits:
    fruits['oranges'] = 0
fruits['oranges'] +=1

print(fruits)

# there's a built-in method as well for this which can be used with 'in' or 'not in'
# whatever suitable
if 'mangoes' not in fruits:
    fruits.setdefault('mangoes',0)
fruits['mangoes'] += 1

print(fruits)