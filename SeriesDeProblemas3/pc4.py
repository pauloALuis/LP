"""
pc4.py
21/08/2021
"""

#4.a)
def f1(f: float = 2.29269235):
    """
    method that format a float to 2 decimal cases and in the center of 40 spaces
    @aparam f : the float
    @return the float formated
    """
    return "{:^40.2f}".format(f)

print(f1())

#4.b)
def f2(a: int, b : int):
    """
    method that converts the first int to hexa and second int to octa using format()
    @param a : an integer
    @param b : an integer
    @return a string with two integers converted
    """
    return "{0:02x} - {1:o}".format(a, b)
print(f2(100 ,100))

#4.c)
def f3(f : float = 2.237464376):
    """
    method that returns a string with two decimal cases align at right
    also formats the stirng with 40 spaces with the letter $
    @param f : float
    @return string converted with format() function
    """
    return "{:$>40.2f}".format(f)

print(f3())

#4.d)
def f4(f: float = 2./3):
    """
    method that uses format( to pass a value to percentage with 2 decimal cases
    @param f : the float
    @reutrn string with percentage of float "f"
    """
    return "{:.2%}".format(f)

print(f4())