# To store values in the memory, we need variables.
# variables assignment
a = 5    # value 5(on RHS) is assigned to the variable a(on LHS)
print(a)

# when we try to assign the same variable with dif values
a = 10
print(a)  # variable a consists of latest value assigned to it

# Also it's imp to declare a variable before it gets printed else throws a NameError
print(b)      # NameError: name 'b' is not defined
b = "Python"

# we might be using same data multiple times in a code
# Instead of using hardcoded path to manually write the same data redundant times in a program
# we can make use of variables
name = "User"
print("Welcome to the Python Programming " + name + "!")
print("Let's start with the practice, "+name)

# variable names in Python have some rules to be followed:
# var name can only consist of letters,nums & underscore
# var name can not start with a letter
# var names are case-sensitive
# var name must not be Python keywords
# It is also recommended to assign a proper name for a variable according to the value it consists of
name = "Joe"
country = "UK"
age = 96

