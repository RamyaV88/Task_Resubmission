# Task 5 - Lambda function
#
# 1. Created a dictionary with a set of names and their age, used lambda filter
# to filter out people below 18 years and printed the list of people above 18 in a list

dictionary = [
    {"Name": "Diana", "Age": 25},
    {"Name": "Alice", "Age": 10},
    {"Name": "Dora", "Age": 15},
    {"Name": "Cindrella", "Age": 30}
]

filtered_people = list(map(lambda people: people if people["Age"] > 18 else None, dictionary))
filtered_people = [people for people in filtered_people if people is not None]

print(f"People above 18 years:",(filtered_people))


# 2. Using Reduce and Lambda function to find the product of all numbers in a list

from functools import reduce

list = [5, 2, 3, 10]
reduced_list = reduce(lambda x, y: x * y, list)
print(f"Product of all numbers on the list is : {reduced_list}")


# 3. Lambda function to check if even numbers from a list and square the even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(f"Numbers are : {numbers}")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEven numbers from the list: {even_numbers}")
square_even = list(map(lambda x: x**2, even_numbers))
print(f"\nSquare of the even numbers from the list: {square_even}")



# 4. Lambda function to check if given string is a number

is_number = lambda q: q.replace('.', '', 1).isdigit()

print(is_number('26587'))
print(is_number('green'))


# 5. Lambda function to extract year, month and day from datetime object
import datetime

now = datetime.datetime.now()
print(now)

# Define a lambda function to extract 'year', 'month' and 'day' from a given datetime object 'x'
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day

# Print the year, month and day extracted from the current datetime object 'now'
print(f"Year:",year(now))
print(f"Month:", month(now))
print(f"Day:",day(now))

# 6. Lambda function to generate a Fibonacci series upto n terms, considering n as 12

def fibonacci(count):
   list_fibonacci = [0, 1]

   any(map(lambda _:list_fibonacci.append(sum(list_fibonacci[-2:])),
         range(2, count)))

   return list_fibonacci[:count]

print(fibonacci(12))

