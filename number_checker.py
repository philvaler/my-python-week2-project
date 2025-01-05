# Challenge: Write a program that checks whether a number is: 1) Positive, negative, or zero. 2) Even or odd. 3) Combine these checks for a detailed output.
# Deliverables: Evaluate a number's properties (positive/negative/zero, odd/even)

favorite_number = input("What is your favorite number? Enter here 👉: ")

try:
    favorite_integer = int(favorite_number)
    modulo_integer = favorite_integer % 2
    
    if favorite_integer < 0 and modulo_integer == 0:
        print(f"Your favorite number is a negative number! It is also an even number! ➖🔢")
    elif favorite_integer < 0 and modulo_integer != 0:
        print(f"Your favorite number is a negative number! It is also an odd number! ➖🔢")
    elif favorite_integer == 0:
        print(f"Your favorite number is zero! 0️⃣")
    elif favorite_integer > 0 and modulo_integer == 0:
        print(f"Your favorite number is a positive number! It is also an even number! ➕🔢")
    else:
        print(f"Your favorite number is a positive number! It is also an odd number! ➕🔢")
except ValueError:
    print(f"You entered in a non-number! 🔤 I'm sorry. Please try again later. Goodbye! 👋")