def max_from_list(numbers):
    max=numbers[0]
    for i in numbers:
        if i>=max:
            max=i
    return max

def min_from_list(numbers):
    min=numbers[0]
    for i in numbers:
        if i<=min:
            min=i
    return min


