from datetime import datetime
import random
import time

#list of odd numbers
odd_numbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,
               33,35,37,39,41,43,45,47,49,51,53,55,57,59]

#for loop suite
for i in range(5):
    #generate a random number
    random_number = random.randint(0,60)

    #get the current minute from datetime module
    this_minute = datetime.today().minute

    print (this_minute)
    #if-else suite
    if this_minute in odd_numbers:
        print ('this is an odd minute')
    else:
        print ('this is an even minute')

    #put for loop to sleep for some random seconds
    print (random_number)
    time.sleep(random_number)
