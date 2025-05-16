# Guvi - Task 4

# 9. Program to find the triplet in list whose sum is equal to 59
# Using combinations() method from itertools module to find the triplet in the list whose sum is equal to 59
# Importing combinations() method from itertools module

from itertools import combinations

def findTriplets(num1_list, key):

    def valid(value):
        return sum(value)== key

    return list(filter(valid, list(combinations(num1_list, 3))))

num1_list = [10,20,30,9]
print(findTriplets(num1_list, 59))


# 1. Program to create a list for all the even numbers and another list for all the odd numbers from the given set of numbers
# Defining a list of numbers
list_number = [10,501,22,37,100,999,87,351]

even = list(filter(lambda num: num % 2 == 0, list_number))
print(f"Even numbers are:",(even))

odd = list(filter(lambda num: num % 2 == 1, list_number))
print(f"Odd numbers are:",(odd))

# 2. Program to create a list for all the Prime numbers from the set of numbers given
# Checking if the number is prime or not by using modulus operator in for loop

mylist=[10,501,22,37,100,999,87,351]
prime_no=[]
for i in mylist :
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count==1:
        prime_no.append(i)
print(f"Prime numbers from the given list:",(prime_no))

# 4. Python program to add the first and the last digit of an integer
# Using positive and negative indexing to get the first and last digit of the number
# Defining a three digit number
number = input("Enter a three digit number: ")

number = str(number)
first_digit = int(number[0])
last_digit = int(number[-1])
sum = first_digit + last_digit

print(f"Sum of the first and last digit of the number {number} is", sum)

#6. To find the duplicates from the given lists
# Defining three lists of numbers

list1 = [11, 12, 13, 14, 15, 16, 17]
list2 = [14, 15, 16, 17, 18]
list3 = [11,13,15,17,19]

common = list(set(list1) & set(list2) & set(list3))
print(f"The duplicates in the given three list are", common)

# 8. Program to find the minimum element of the sorted and rated list from the numbers that are displayed below:
# Defining a list of numbers
# Sorting the list using sort() method which sorts the list in ascending order
# and then printing the first element of the sorted list
list1 = [18,84,6,89,99]

list1.sort()
print("The sorted list is:", list1)
# Printing the first element of the sorted list which is the minimum element

print("The minimum element of the sorted list is:", list1[0])

# 10. Program to find if there is a sublist with sum equal to zero
# Using set() to find if there is a sublist with sum equal to zero
# and then using for loop to iterate through the list

def subArrayExists(arr, length):
    # Create an empty set to store the prefix sums
    n_sum = 0
    sum = set()
    for i in range(length):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in sum:
            return True
        sum.add(n_sum)
    return False
arr = [4, 2, -3, 1, 6]
length = len(arr)
if subArrayExists(arr, length) == True:
    print("Found a subarray with sum as 0")
else:
    print("No such sub array exits!")

