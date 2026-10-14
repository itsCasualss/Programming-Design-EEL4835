
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)
print(sum_digits(1234))


# Modulos and Integer Division
# n%10 -> gets the last digit
# e.g. 1234 % 10 = 4

# n // 10 -> removes the last digit.
# e.g. 1234 // 10 = 123 
