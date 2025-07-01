def my_function():
    ' ' 'Demonstrates triple double quotes docstrings and does nothing really' ' '
 
    return None

print("Using __doc__:")
print(my_function.__doc__)

# print("Using help:")
# help(my_function)


def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b
print(multiply_numbers(3,5))


def power(a, b):
    ' ' 'Returns arg1 raised to power arg2.' ' '
 
    return a**b

print((power.__doc__),power(5,3))




class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
        real (int): The real part of the complex number.
        imag (int): The imaginary part of the complex number.
    """

    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.

        Parameters:
            real (int): The real part of the complex number.
            imag (int): The imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag

    def add(self, num):
        """
        The function to add two Complex Numbers.

        Parameters:
            num (ComplexNumber): The complex number to be added.

        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
        re = self.real + num.real
        im = self.imag + num.imag

        return ComplexNumber(re, im)

# Access the Class docstring using help()
help(ComplexNumber)

# Access the method docstring using help()
help(ComplexNumber.add)


