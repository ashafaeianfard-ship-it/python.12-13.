def zarb(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result

print(zarb([1, 20, 5, 6, 9, 10]))