#dictionary example
found = {'a':0,'e':0,'i':0,'o':0,'u':0}

word = 'Milkiway'

for char in word:
    if char in found:
        found[char] += 1

# this will print complete dictionary but in raw format like
# {'a': 1, 'e': 0, 'i': 2, 'o': 0, 'u': 0}
print(found)

# now if we want to print it in a better way then
for kv in found:
    print(kv,':',found[kv])