############################################################################################################################

# 1. Create a string variable called greeting and show it 5 times
greeting = "Bonjour! ,"
result = greeting * 5
print(result)

# 2. Function to print the sum 5 + 4 + 3 + 2 + 1 recursively
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

# Call the recursive function and print result
sum_result = recursive_sum(5)
print(sum_result)

# 3. Loop to print 1, 4, 9, 16, 25
for i in range(1, 6):
    print(i * i)

# 4. Create a class Person with a constructor for age and a method to print age
class Person:
    def __init__(self, age):
        self.age = age

    def print_age(self):
        print(f"My age is {self.age}")

# Create instance and call the print_age method
person = Person(30)
person.print_age()

# 5. Throw and catch an error, then print a caught message
try:
    raise ValueError("An intentional error")
except ValueError as e:
    print(f"Error caught: {e}")

# 6. Create a method with a default parameter value
def today(day="Friday"):
    print(f"Today is {day}")

# Call the method with and without argument
today()
today("Monday")

# 7. While loop that counts down from 10 to 1
counter = 10
while counter > 0:
    print(counter)
    counter -= 1

# 8. Create a list and tuple, print the last value, try changing first value of tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Print the last values
print(my_list[-1])
print(my_tuple[-1])

# Modify the list's first value
my_list[0] = 7
print(my_list)

# Attempt to modify the tuple's first value will result in error (tuples are immutable)
try:
    my_tuple[0] = 7
except TypeError as e:
    print(f"Error: {e}")

# Comment on issue: "Tuples are immutable, so their values cannot be changed."

# 9. Create a dictionary named store with name, city, and avg_price
store = {
    "name": "SuperMart",
    "city": "Abidjan",
    "avg_price": 8.800
}
print(store)

# 10. One-line if-else condition to check if a number is even or odd
num = 5
print("Even" if num % 2 == 0 else "Odd")

# 11. Create an empty list and add the first 5 even numbers dynamically
even_numbers = []
for i in range(2, 12, 2):
    even_numbers.append(i)
print(even_numbers)

# 12. Print the last value of a list using a negative index
print(even_numbers[-1])

# 13. Convert a float 20.5 to int
int_value = int(20.5)
print(int_value)

# 14. Block of comments and single line comment
"""
This is a block of comments
explaining the code and its purpose.
It spans multiple lines.
"""
# This is a single line comment

# 15. Use chr() function to print the entire alphabet from a-z
for i in range(97, 123):
    print(chr(i), end=" ")  # chr(97) = 'a', chr(122) = 'z'
