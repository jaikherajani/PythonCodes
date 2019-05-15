# copying lists

# new list
list1 = [1,2,3,4,5,6,7,8,9]

# this copies only the reference so whatever changes we make here
# in list1 will be reflected in list2 as well and vice-versa
list2 = list1

list2.append(0)

print('list1',list1)
print('list2',list2)

# to really copy a list we should use copy()
list3 = list1.copy()

list3.pop()

print('-----------------------------------------')
print('list1',list1)
print('list2',list2)
print('list3',list3)
