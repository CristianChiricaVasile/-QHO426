"""print("Calculating the sum of the first 100 numbers..")
sum_total = 0

number = 1

while number < 100:
    sum_total = sum_total + number
    number = number + 1

print("...Done! The answer is " , sum_total) """


print("How many numbers should I sum up?")

    # Get the count of numbers to sum up
    count = int(input())
    print()  # Print a blank line for better readability

    # Initialize variables
    total = 0  # Variable to store the running sum
    current = 1  # Counter to track which number we're collecting

    # Loop to collect each number
    while current <= count:
        # Prompt user for the current number
        print(f"Please enter number {current} of {count}:")

        # Get the number and add it to our total
        number = float(input())
        total += number

        # Move to the next number
        current += 1

    print()  # Print a blank line for better readability

    # Display the final sum
    print(f"The answer is {total}.")


# Run the program
if __name__ == "__main__":



