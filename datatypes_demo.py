print("Name :- Yash Sunil Lohar")

# 1. Different data types

integer_a = 10
float_b = 3.14
string_c = "Hello"
boolean_d = True

# 2. Print type of each variable
print("Initial variable and their types:- ")
print("Integer :- ", integer_a, "->", type(integer_a))
print("Float   :- ", float_b, "->", type(float_b))
print("String  :- ", string_c, "->", type(string_c))
print("Boolean :- ", boolean_d, "->", type(boolean_d))

print("\n-----------------------------------------------------")

# 3. Perform arithmetic operations using numeric variables
print("Arithmetic Operations:")
print("Addition:", integer_a + float_b)
print("Subtraction:", integer_a - float_b)
print("Multiplication:", integer_a * float_b)
print("Division:", integer_a / float_b)

print("\n-----------------------------------------------------")

# 4. Taking string input and converting using type casting

try:
    user_int = input("Enter integer number:- ")
    user_float = input("Enter floating point number:- ")

    # Convert string input to integer and float
    # input() always returns string, so we must convert it
    num1 = int(user_int)
    num2 = float(user_float)

    print("\nType after conversion:- ")
    print("num1 =", num1, "->", type(num1))
    print("num2 =", num2, "->", type(num2))

    # 5. Use converted values in calculation
    print("\nSum of num1 and num2 =", num1 + num2)

except ValueError:
    # 6. Handle invalid input using basic error handling
    print("Invalid input! Enter numbers only.")

print("\n-----------------------------------------------------")

# 7. String and number concatenation

age = 23
print("My age is " + str(age))

print("\n-----------------------------------------------------")

# 8. Demonstrate dynamic typing in Python

x = 100
print("x =", x, "->", type(x))

# Reassigning same variable to a different type
x = "Yash"
print("x =", x, "->", type(x))

x = 3.5
print("x =", x, "->", type(x))

print("\n-----------------------------------")

print("Program executed successfully!")
