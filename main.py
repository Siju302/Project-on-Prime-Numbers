def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all 2-digit prime numbers
print("Two-digit prime numbers are:")
for number in range(10, 100):
    if is_prime(number):
        print(number, end=" ")
