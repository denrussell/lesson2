#  Task1 - You are provided with a Python script that uses conditional statements to tell 
# if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

number = int(input("Enter a number: "))   # I added the int command here to automatically take the integer input and not string.

if number > 0:
    print("The number is positive.")
elif number == 0:         # I added a second equal sign here to make it a comparison that means the same as.
    print("The number is zero.")
else:                     # I ommitted everything else and just put else because if it doesn't satisfy if and elif, everything else falls here.
    print("The number is negative.")