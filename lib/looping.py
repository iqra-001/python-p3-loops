# !/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")


    # code goes here!


def square_integers(int_list):
    squared_list= []
    for num in int_list:
        squared_list.append(num **2)
    return squared_list        
    
print(square_integers([1,2,3,4,5]))
    # code goes here!
    
# numbers = (1, 100)
def fizzbuzz():
    for num in range (1, 101):
       if (num % 3 == 0) and (num % 5 == 0):
        print ("FizzBuzz")
       elif num % 3 == 0:
        print ("Fizz")
       elif num % 5 == 0:
        print ("Buzz")
       else:
        print (num)       
    
fizzbuzz()  # code goes here!
    
