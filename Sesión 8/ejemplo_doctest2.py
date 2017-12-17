# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:39:52 2017

@author: silve
"""

def square(x):
    """
    Esta función eleva un número al cuadrado
    >>> square(-3)
    9
    >>> square(16)
    Traceback (most recent call last):
      ...
    ValueError: input too large
    """
    if x > 10:
        raise ValueError('input too large')
    else:
        return x*x
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)