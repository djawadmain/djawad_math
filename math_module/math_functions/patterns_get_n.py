from .decorators import single_member_list_to_integer


@single_member_list_to_integer
def fibonacci(number):
    """
    this function for fibonacci pattern
    like this ==>
    0, 1, 1, 2, 3, 5, 8, 13, ...
    and fib(n) = fib(n - 1) + fib(n - 2)
    """

    if number < 1:
        raise ValueError('Please enter number upper than 0')

    # set first numbers
    a, b = 0, 1

    # loop for get fib(n)
    for i in range(number):
        a, b = b, a + b

    return b


@single_member_list_to_integer
def sum_numbers(number):
    """
    this function for calculate sum(1...number)
    and use gauss formula (count * mean)
    """
    count = number
    mean = (number + 1) / 2

    result = count * mean

    return int(result)
