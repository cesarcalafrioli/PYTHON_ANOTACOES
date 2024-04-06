"""
Execute the following command line:
black -l 79 *.py
"""
def my_function(name):
    """
    >>> my_function('black')
    'received Black'
    """
    return "received {0}".format(name.title())
