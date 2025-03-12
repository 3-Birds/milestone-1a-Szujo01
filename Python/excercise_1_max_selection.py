#Write a Python function to find the maximum element in a list of numbers without using the built-in `max()` function.
#If the input list is None or it is empty list, the return value must be None.

# Requirements:
# - Returns greatest element of a list of numbers
# - In case of None input returns None
# - In case of Empty input string, returns None

numbers = [2,9,6,3]

def get_max(numbers:list) -> int:
    if numbers is None or len(numbers) == 0:
        return None
    else:
        max = numbers[0]
        for i in numbers:
            if i > max:
                max = i
        return max

print("The list elements are : " , numbers)
print("The greatest element is : " , get_max(numbers))
