# Problem 19: Convert Decimal to Binary

# Write a Python function that takes a decimal (base-10) integer and returns its binary (base-2)
# equivalent as a string.


def convert_binary (number: int) -> str:
    in_bin: str = ""
    while(number != 1):
        rem: str = str(number % 2)
        number = number // 2
        in_bin = rem + in_bin

    in_bin = "1" + in_bin
    return in_bin


print(convert_binary(100))

