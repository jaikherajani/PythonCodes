# list : an ordered mutable collection of objects
# it is just like an array but is dynamic in nature and heterogenous

# list of vowels
vowels = ['a','e','i','o','u']

# an empty list
el = []

# word in which we have to check for vowels
word = "Milkiway"

# "in" is used to see if something is inside of some other thing
# for loop suite
for letter in word:
    if letter in vowels:
        print('found',letter)

# we can also use "not in" to check that something should not be inside of something else 
# here we will use it to append only unique vowels to the list
# for loop suite
for letter in word:
    if letter in vowels:
        if letter not in el:
            el.append(letter)
            print('list is',el)
 