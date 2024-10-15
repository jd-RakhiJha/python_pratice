def check_even_odd(arr):
    # Manually calculate the length of the array
    length = 0
    for _ in arr:
        length += 1

    # Create lists to store even and odd numbers
    even_numbers = []
    odd_numbers = []

    # Iterate through the array to determine even or odd
    for i in range(length):
        # Check if the current number is even or odd
        if (arr[i] // 2) * 2 == arr[i]:  # If double the integer division is equal to the number
            even_numbers.append(arr[i])
        else:
            odd_numbers.append(arr[i])

    return even_numbers, odd_numbers

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
evens, odds = check_even_odd(arr)
print("Even numbers:", evens)
print("Odd numbers:", odds)

