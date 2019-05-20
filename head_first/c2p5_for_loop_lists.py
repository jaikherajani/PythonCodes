# for loop understands the lists

paranoid_android = 'Marvin, the paranoid android'
letters = list(paranoid_android)

# for loop automatically detects the lists and works accordingly
for alph in letters:
    print(alph)

#for loop also detects the slices of the lists
for alph in letters[:6]:
    print('\t',alph)

print()

for alph in letters[-7:]:
    print('\t'*2,alph)

print()

for alph in letters[12:20]:
    print('\t'*3,alph)
