# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    return (n % 2 == 0)

# Read a number from the keyboard
num = input("Enter a number: ")
try:
    num = int(num)
except:
    print("Requires a number")
    exit(1)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print("Even!" if is_even(num) else "Odd")
