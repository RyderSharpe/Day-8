# Functions with Inputs - Python Notes

# 1. Defining a Function
def greet(name):
    print(f"Hello, {name}!")

# 2. Calling a Function
greet("Alice")

# 3. Parameters vs Arguments
def add(a, b):  # a and b are parameters
    return a + b

result = add(5, 3)  # 5 and 3 are arguments

# 4. Default Values
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Outputs: Hello, Guest!

# 5. Return Statement
def add_and_multiply(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

result_sum, result_product = add_and_multiply(3, 4)

# 6. Scope of Variables
global_var = 10

def my_function():
    local_var = 5
    print(global_var)  # Accessible
    print(local_var)   # Accessible

my_function()
print(global_var)  # Accessible
# print(local_var)  # Error: NameError (local_var is local to the function)

# 7. Arbitrary Number of Arguments
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, "hello")
