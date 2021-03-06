# Lab 1.1

"""
# input = [10,20,3,3]
# input = [15,14,2,3]
input_string = input("Input array of numbers (separated by space): ")
nums = [int(i) for i in input_string.split()]
# print(input_string)
# print(nums)
output = (( nums[0] + nums[1] ) // nums[2]) * nums[3]
print(output)
"""

# Lab 1.2

"""
def concatenate(char1, char2, char3):
    string = char1 + char2 + char3
    print(string)

concatenate("a", "b", "c")
concatenate("%", "2", "o")
concatenate("1", "5", "p")
"""

# Lab 1.3
"""
def elevator(n, p):
    if (n % p == 0):
        return n // p
    else:
        return n // p + 1

print(elevator(17, 3))
print(elevator(4, 5))
print(elevator(10, 5))
"""

# Lab 1.4
"""
def sum_ascii(chars):
    return sum(ord(c) for c in chars)

# chars = "AbCdE"
# chars = "SoftUniRulzz"

n = int(input("Input number of lines, and characters to sum, each input on a separate line (followed by RETURN):\n"))
chars = "".join(input() for _ in range(n))

print("The sum equals:", sum_ascii(chars))
 """

# Lab 1.5

def print_ascii(char):
    print(ord(ascii))

# n, m = (60, 65)
# n, m = (69, 79)
# n, m = (97, 104)
# n, m = (40, 55)

start = int(input("Input first ASCII character index: "))
stop = int(input("Input last ASCII character index: "))

for i in range(start, stop+1):
    print(chr(i), end="")
print("")