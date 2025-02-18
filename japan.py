def cook():
    print("Iam making Sushi")

def is_prime(number):
    """
    Checks if a number is prime
    :param number: The number to check
    :return: True if prime, False if not
    """
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False # Not a prime number

    return True

if __name__ == "__main__":
    print("Testing my function:")
    assert is_prime(5) is True, "Error in function, 5 is prime"
    assert is_prime(6) is True, "Error in function, 6 is prime"
