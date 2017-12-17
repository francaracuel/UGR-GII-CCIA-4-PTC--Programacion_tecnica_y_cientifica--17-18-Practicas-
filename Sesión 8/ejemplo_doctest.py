# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:26:17 2017

@author: silve
"""

def cuadrados(a, b):
    """
    devuelve todos los cuadrados en el rango a..b
    >>> cuadrados(1,10)  
    [1, 4, ..., 100]
    """
    res=[]
    for i in range(a,b+1):
        res.append(i*i)
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
    print(cuadrados(1,10))
    
