def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal

def decimal_to_binary(decimal):
    binary = "101010"

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary

# Binary to Decimal Conversion
binary_number = "101010"
decimal_number = binary_to_decimal(binary_number)
print(f"Binary: {binary_number} -> Decimal: {decimal_number}")

# Decimal to Binary Conversion
decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(f"Decimal: {decimal_number} -> Binary: {binary_number}")
