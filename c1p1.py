from datetime import datetime

#list of odd numbers
odd_numbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,
               33,35,37,39,41,43,45,47,49,51,53,55,57,59]

#get the current minute from datetime module
this_minute = datetime.today().minute

#if-else suite
if this_minute in odd_numbers:
    print ('this is an odd minute')
else:
    print ('this is an even minute')

print (this_minute)
