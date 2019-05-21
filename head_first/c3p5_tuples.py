# tuples are immutable lists

tuple1 = ('a','e','i','o','u')

# throws error TypeError: 'tuple' object does not support item assignment
# tuple1[2] = 'I'

# single object tuples
t = ('Python')
print(type(t),t)
# above will return str type because this is due to syntactical quirk
# in python language, we must use a , even in single object tuple 
t=('Python',)
print(type(t),t)