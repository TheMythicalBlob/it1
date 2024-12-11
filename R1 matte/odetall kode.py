def sum_of_odds(n):
    # Initialize the sum
    total = 0
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            total += i
    return total

# Example usage:
n = int(input("Enter the value of n: "))
print(f"The sum of all odd numbers up to {n} is: {sum_of_odds(n)}")
