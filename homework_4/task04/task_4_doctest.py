from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function takes a number N as an input and returns N FizzBuzz numbers.
     - Install Python 3.9 (https://www.python.org/downloads/)
     - Install pytest `pip install pytest`
     - Clone the repository https://github.com/guzvladimir/epam_homeworks
     - Checkout branch homework_4
     - Open terminal
     - Run: pytest --doctest-modules homework_4/task04/task_4_doctest.py

     >>> fizzbuzz(5)
     ['1', '2', 'fizz', '4', 'buzz']
     >>> fizzbuzz(15)
     ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']
     >>> fizzbuzz(-5)
     []
     >>> fizzbuzz(1.5)
     Traceback (most recent call last):
     ...
     TypeError: 'float' object cannot be interpreted as an integer
    """
    fizzbuzz_numbers = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            fizzbuzz_numbers.append("fizz buzz")
        elif number % 3 == 0:
            fizzbuzz_numbers.append("fizz")
        elif number % 5 == 0:
            fizzbuzz_numbers.append("buzz")
        else:
            fizzbuzz_numbers.append(str(number))
    return fizzbuzz_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
