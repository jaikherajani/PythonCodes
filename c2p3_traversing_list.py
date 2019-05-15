# traversing lists

# method 1
# lists can be traversed by using listname[index]
# lists support positive index starting from 0 as well as
# negative index starting from -1

saying = "Don't Panic!"

# converting string to list
letters = list(saying)

print('Saying',saying)
print('letters',letters)

# traversing list using index
print('index 0',letters[0])
print('index 1',letters[1])
print('index 4',letters[4])
print('index 7',letters[7])
print('index -1',letters[-1])
print('index -3',letters[-3])
print('index -6',letters[-6])

print('-------------------------------------------------------')

# method 2
# lists can also be traversed by using listname[start,stop,step]
# it starts fro starting index, stops at stop index excluding stop
# and step means how many elements to skip between each iteration

# print complete list
print('letters',letters)

# print every 3rd letter from 0 to 10 (but not inlcuding 10)
print('letters[0:10:3]',letters[0:10:3])

# skip first 3 and print everythig else
print('letters[3:]',letters[3:])

# all letters upto but not including indx location 10
print('letters[:10]',letters[:10])

# print every second letters
print('letters[::2]',letters[::2])

# printing list in reverse order
print('letters[::-1]',letters[::-1])
print('above list in string',''.join(letters[::-1]))
