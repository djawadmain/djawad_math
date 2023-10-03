from functools import wraps


# smlti is single_member_list_to_integer function
def check_error_for_smlti(lst: list):
    """
    this function for exception and errors of
    single_member_list_to_integer function and
    handel TypeError for not list set and ValueError for value of index and length of lst
    """

    lst_type = type(lst)
    lst_length = len(lst)

    if lst_type != list:
        raise TypeError(f'Please send list to function not {lst_type}')

    if lst_length != 1:
        raise ValueError(f'Please enter list with one argument not {lst_length}')

    lst_first_index = lst[0]

    if not lst_first_index.isnumeric():
        raise ValueError(f'Please set positive number for argument {lst_first_index} is not positive integer')


def single_member_list_to_integer(function):
    """
    this decorator make it easy function works for
    set [<int>] to <int> with handel errors and exceptions
    """

    @wraps(function)
    def wrapper(lst: list):
        check_error_for_smlti(lst)

        argument_for_function = int(lst[0])

        return function(argument_for_function)

    return wrapper
