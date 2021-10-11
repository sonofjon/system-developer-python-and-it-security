def even_numbers(function):
    def wrap(numbers):
        evens = []
        for num in numbers:
            if num%2 == 0:
                evens.append(num)
        return function(evens)
    return wrap

@even_numbers   # identical to: print_numbers = even_numbers(print_numbers)
def print_numbers(numbers):
    print(numbers)

print_numbers([1,2,3,4,5])