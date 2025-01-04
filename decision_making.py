# Task 1: Introduction to Conditional Statements: Review syntax of `if`, `elif`, and `else``
age = 20
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

### Task 2: Write Your First Conditional Program: Write a script that 1) Asks the user's age using `input()`. 
# 2) Uses `if/elif/else` to print whether the user is a child, teen, or adult.
try:
    user_age = int(input("Write down your age right after this sentence. "))

    if user_age <= 1:
        print("You are a baby! 🐣 Goo goo gah gah!")
    elif user_age <= 3:
        print("You are a toddler! 👶 Baby Shark! 🦈")
    elif user_age <= 5:
        print("You are a preschooler! 🚌 The wheels on the bus go 'round, 'round, 'round! 🛞")
    elif user_age <= 9:
        print("You are a child! 🧒👧 You must have a lot of friends at school!")
    elif user_age <= 12:
        print("You are a tween! 🌟 You are growing up very fast!")
    elif user_age <= 19:
        print("You are a teen! 🙇 I bet you still haven't figured who you are yet! 🫵")
    elif user_age <= 29:
        print("You are a young adult! 🤯 Buckle up! It's about to get weird!")
    elif user_age <= 64:
        print("You are an adult! 🥂 Life still doesn't make sense! 😭")
    else:
        print("This is it! You are a senior citizen! 👴👵 You better have a loved one next to you so you aren't lonely!")
except ValueError:
    print("Did you think I wouldn't notice? Come on now! Write your age! Don't be so presumptious! 😡")