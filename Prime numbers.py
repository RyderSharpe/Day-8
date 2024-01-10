# TODO-Write your code below this line 👇

list = [2,3,4,5,6,7,8,9,10]

def prime_checker(number):

    for prime in list:

        if number % prime == 0:
            print("It's not a prime number.")
            break
    else:
         print("It's a prime number.")
        
# Write your code above this line 👆
# Do NOT change any of the code below👇

n = int(input())  # Check this number
prime_checker(number=n)
