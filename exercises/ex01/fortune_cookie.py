"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730368118"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 



from random import randint
print("your fortune cookie says...")
x = (randint(1, 30))
if x >= 16:
    print("You will discover new riches")
else:
    if x == 15:
        print("You will recieve everything you ever wanted")
    else:
        if x == 14
            print("You get three wishes provided by a genie")
        else:
            print("You will be blessed with good vibes for a week")