import sys

from math_functions import fibonacci, sum_numbers

# def argv_function_handler(function_name, function_arguments):
#     print(function_name)
#     if function_name in ['fibonacci']:
#         if function_name == 'fibonacci':
#             result = fibonacci(function_arguments)
#
#         print(result)
#
#     else:
#         NameError('Please write correct function this function is not defined')


def main() -> None:
    argv = sys.argv

    if len(argv) >= 3:
        try:
            exec(f"""print({argv[1]}({argv[2:]}))""")

        except NameError:
            print('Please write correct function this function is not defined')


if __name__ == '__main__':
    main()
