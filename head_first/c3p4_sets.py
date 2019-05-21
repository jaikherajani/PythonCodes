# sets don't allow duplicates, order is not guaranteed
vowels = {'a','a','e','e','i','o','u','u'}

# duplicates will be removed {'a', 'i', 'e', 'u', 'o'}
print(vowels)

# set from string
vowels1 = set('aeeeeeeeiou')
print(vowels1)

# set operations
word = 'hello'
vowels2 = set('aeiou')

# union {'e', 'l', 'o', 'h', 'i', 'a', 'u'}
u = vowels2.union(set(word))
print(u)

# difference {'a', 'u', 'i'}
d = vowels2.difference(set(word))
print(d)

# intersection {'o', 'e'}
i = vowels2.intersection(set(word))
print(i)