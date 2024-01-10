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


################ HOW IT WORKS##################

# You define a list called list containing numbers from 2 to 10.
# You create a function prime_checker that takes a number as an argument.
# Inside the function, you use a for loop to iterate over each element in the list.
# In each iteration, you check if the given number (n) is divisible evenly by the current prime from the list using the modulus operator (%).
# If the number is divisible, you print "It's not a prime number." and use the break statement to exit the loop.
# If the loop completes without finding any divisor, the else block is executed, and you print "It's a prime number."
# Finally, you take user input for a number (n) and call the prime_checker function with that input.
