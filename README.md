Python Data Types & Type Casting Demo

Author: Yash Lohar

This project is a practical implementation of Python's fundamental data types. It demonstrates how to declare variables, perform arithmetic across different types, safely handle user input, and showcase Python's dynamic typing capabilities.
________________________________________
🚀 Key Features in the Code
1. Type Inspection
   
The script initializes variables for the four core types and uses type() to verify their class:

    •	Integer (int): integer_a = 10

    •	Float (float): float_b = 3.14

    •	String (str): string_c = "Hello"

    •	Boolean (bool): boolean_d = True

2. Mixed-Type Arithmetic
   
The code performs operations between int and float variables. Python automatically handles "Type Promotion," where the result of an operation between an integer and a float becomes a float.

    •	Operations included: Addition, Subtraction, Multiplication, and Division.
3. Safe Type Casting
   
Since the input() function always returns a string, the script performs manual casting:

    •	int(user_int): Converts text to a whole number.
   
    •	float(user_float): Converts text to a decimal number.
   
    •	Error Handling: A try-except block catches ValueError if a user enters non-numeric text, preventing a program crash.
4. Proper Concatenation
   
The script demonstrates that strings and numbers cannot be added directly. It uses str(age) to convert the integer into a string format before concatenating it with text.

5. Dynamic Typing Demonstration

Unlike statically-typed languages, this script shows how the variable x can seamlessly transition from an Integer (100) to a String ("Yash") and finally to a Float (3.5).

________________________________________
🛠 How to Use
1.	Run the script:
Bash
python datatypes_demo.py
2.	Follow the prompts: Enter an integer and a float when requested.
3.	Test the Error Handling: Try entering a word (like "apple") when asked for a number to see the except block in action.
________________________________________
📊 Sample Output Structure

<img width="832" height="1145" alt="image" src="https://github.com/user-attachments/assets/ed972472-3b3f-45b9-97c8-5ed752dc8e0e" />
