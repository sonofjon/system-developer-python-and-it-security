def decorator_function(original_function):
    def wrapper_function (numbers):
        print(numbers)
        return original_function(numbers)
    return wrapper_function

@decorator_function   # identical to: even_numbers = decorator_func(even_numbers)
def even_numbers(numbers):
    evens = []
    for num in numbers:
        if num%2 == 0:
            evens.append(num)
    return evens
    # print(evens)

# even_numbers([1,2,3,4,5])
print(even_numbers([1,2,3,4,5]))

