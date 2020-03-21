#Write a recursive function that finds the largest number in a given list of integers.

#For this program we could either use a list or a tuple. They are similar but have 1 key differences
#List - Ordered and we can change values
#Tuple - Ordered and we cannot change values


numlist = [21,420,88,69,666,333,7,47]
n = len(numlist)

def large(arr, size):
    if(size == 1):
        return arr[0]
    else:
        return max(arr[size-1], large(arr, size-1))

def main():
    print("The largest number in the list is", large(numlist, n))

main()