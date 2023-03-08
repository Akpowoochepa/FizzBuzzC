Adding comments to the code to allow the users to understand and read the 
code better.

# Loop through the numbers 1 to 100
for num in range(1, 100):
    # Check if the number is divisible by 3
    if num % 3 == 0:
        # Check if the number is also divisible by 5
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    # Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    # If the number is not divisible by 3 or 5, print the number itself
    else:
        print(num)


