#Write a recursive function that finds the largest number in a given list of integers.

#For this program we could either use a list or a tuple. They are similar but have 1 key differences
#List - Ordered and we can change values
#Tuple - Ordered and we cannot change values


numlist = [21,420,88,69,666,333,7,47]

def large:
    if(len(numlist) == 0):
        print("This is an empty list.")
    if(len(numlist) == 1):
        print("The largest number is", numlist[0])
    else:
        