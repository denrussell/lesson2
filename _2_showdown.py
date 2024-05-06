# Objective:
# Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest number 
# among the three and print it out.

# Task 3: Equality Check
# Enhance your program to handle cases where two or all of the numbers are equal. 
# The program should display appropriate messages like "Two numbers are equal 
# and the largest" or "All numbers are equal".

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should 
# print out that "The smallest number is 3. 
# The largest number is 4. There are two numbers equal to each other." 
# Printing out which numbers are equal would be a great added bonus.

# Okay so I after 3 days of thinking and lots of trial and errors.
# I finally came up with a finished product. I know my knowledge is limited for now.
# I know I don't have all the tools for now. I only know what I know.
# But tt was fun!
# I tested them all to see if they all work well.


# Asking user to enter 3 numbers.
print("Please enter 3 numbers:")
num1 = int(input("1st: "))
num2 = int(input("2nd: "))
num3 = int(input("3rd: "))

# I assigned variables to the numbers that are equal.
e1e2 = num1 == num2      # numbers 1 and 2 are equal
e1e3 = num1 == num3      # numbers 1 and 3 are equal
e2e3 = num2 == num3      # numbers 2 and 3 are equal

# I assigned variables to the largest number.
num3g = num3 > num1 and num3 > num2   # largest number is 3
num2g = num2 > num1 and num2 > num3   # largest number is 2
num1g = num1 > num2 and num1 > num3   # largest number is 1

# I assigned variables to the smallest number.
num3s = num3 < num1 and num3 < num2   # smallest number is 3
num2s = num2 < num1 and num2 < num3   # smallest number is 2
num1s = num1 < num2 and num1 < num3   # smallest number is 1

# if conditions for two numbers that are equal and smaller.
if e1e2 and num3g is True:     
   print("=======Answer========")
   print("The largest number is the 3rd:",num3)
   print("Two numbers are equal and the smaller numbers: 1st and 2nd.")
   print("1st:",num1)
   print("2nd:",num2)
elif e1e3 and num2g is True:
   print("=======Answer========")
   print("The largest number is the 2nd:",num2)
   print("Two numbers are equal and the smaller numbers: 1st and 3rd.")
   print("1st:",num1)
   print("3rd:",num3)
elif e2e3 and num1g is True:
   print("=======Answer========")
   print("The largest number is the 1st:",num1)
   print("Two numbers are equal and the smaller numbers: 2nd and 3rd.")
   print("2nd:",num2)
   print("3rd:",num3)
   
# if conditions for two numbers that are equal and larger.
elif e1e2 and num3s is True:     
   print("=======Answer========")
   print("The smallest number is the 3rd:",num3)
   print("Two numbers are equal and the larger numbers: 1st and 2nd.")
   print("1st:",num1)
   print("2nd:",num2)
elif e1e3 and num2s is True:
   print("=======Answer========")
   print("The smallest number is the 2nd:",num2)
   print("Two numbers are equal and the larger numbers: 1st and 3rd.")
   print("1st:",num1)
   print("3rd:",num3)
elif e2e3 and num1s is True:
   print("=======Answer========")
   print("The smallest number is the 1st:",num1)
   print("Two numbers are equal and the larger numbers: 2nd and 3rd.")
   print("2nd:",num2)
   print("3rd:",num3)

# if condition for all numbers equal.
elif e1e3 and e2e3 is True:
   print("=======Answer========")
   print("All numbers are equal.")

# if conditions for which number is largest and smallest.
elif num3g and num2s is True:                      # 3,2
   print("=======Answer========")
   print("The largest number is the 3rd: ",num3)
   print("The smallest number is the 2nd: ",num2)
elif num3g and num1s is True:                      # 3,1
   print("=======Answer========")
   print("The largest number is the 3rd: ",num3)
   print("The smallest number is the 1st: ",num1)
elif num2g and num3s is True:                       # 2,3
   print("=======Answer========")
   print("The largest number is the 2nd: ",num2)
   print("The smallest number is the 3rd: ",num3)
elif num2g and num1s is True:                       # 2,1
   print("=======Answer========")
   print("The largest number is the 2nd: ",num2)
   print("The smallest number is the 1st: ",num1)
elif num1g and num2s is True:                       # 1,2
   print("=======Answer========")
   print("The largest number is the 1st: ",num1)
   print("The smallest number is the 2nd: ",num2)
elif num1g and num3s is True:                       # 1,3
   print("=======Answer========")
   print("The largest number is the 1st: ",num1)
   print("The smallest number is the 3rd: ",num3)



# The formulas below are the first formula I wrote before finalizing
# after a lot of trial and errors

#elif num2 > num1 and num2 > num3 and num1 > num3:   # 2,3
#   print("The largest number is the 2nd: ",num2)
#   print("The smallest number is the 3rd: ",num3)
#elif num3 > num1 and num3 > num2 and num2 > num1:   # 3,1
#   print("The largest number is 3rd: ",num3)
#   print("The smallest number is 1st: ",num1)
#elif num3 > num1 and num3 > num2 and num1 > num2:   # 3,2
#   print("The largest number is 3rd: ",num3)
#   print("The smallest number is 2nd: ",num2)
#elif num1 > num2 and num1 > num3 and num3 > num2:    # 1,2
#   print("The largest number is the 1st: ",num1)
#   print("The smallest number is 2nd: ",num2)
#elif num2 > num1 and num2 > num3 and num3 > num1:  # 2,1
#   print("The largest number is the 2nd: ",num2) 
#   print("The smallest number is 1st: ",num1)







#if e1e2 and e2e3 and e1e3:
 #   print("All numbers are equal")
#elif e2e3:
 #   print("Two numbers are equal: 2nd-",num2,"and 3rd-",num3)
#elif e1e2:
 #   print("Two numbers are equal: 1st-",num1,"and 2nd-",num2)
#elif e1e3:
 #   print("Two numbers are equal: 1st-",num1,"and 3rd-",num3)

#if g1g2 and g1g3:
 #   print("The largest number is the 1st: ",num1)

#if num3 > num1 < num2:
 #   print("The smallest number is the 1st: ",num1)
#elif num1 > num2 < num3:
 #   print("The smallest number is the 2nd: ",num2)
#else:
 #   print("The smallest number is the 3rd: ",num3)


# Task2
#if num1 < num2 and num1 < num3:
 #   print("The smallest number is the 1st: ",num1)
#elif num2 < num1 and num2 < num3:
 #   print("The smallest number is the 2nd: ",num2)
#else:
 #   print("The smallest number is the 3rd: ",num3)

# Task3
#if num1 == num2 == num3:
 #   print("All numbers are equal. 1st, 2nd, 3rd: ",num1)
#elif num1 == num2 or num1 == num3:
 #   print("Two numbers are equal to each other.")