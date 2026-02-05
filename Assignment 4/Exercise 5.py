def remove_even(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n)
    return result


# Main program for testing
original_list = [1, 2, 3, 4, 5, 6, 7]
new_list = remove_even(original_list)

print("Original list:", original_list)
print("List without even numbers:", new_list)
