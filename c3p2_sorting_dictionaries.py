# suppose we create a dictionary like this -

# empty dictionary
found = {}

# adding key values to dictionary
found['a'] = 0
found['i'] = 0
found['e'] = 0
found['u'] = 0
found['o'] = 0

# printing it will give it in a random order
# since in dictionaries order might not be preserved
print(found)

# so we use sorted() to return a sorted dictionary
print(sorted(found))

# it can also be used with loop
for k,v in sorted(found.items()):
    print(k,':',v)