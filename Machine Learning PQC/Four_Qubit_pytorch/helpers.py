# This file contains some helper functions for us

def binary(x):
    return ('0'*(4-len('{:b}'.format(x) ))+'{:b}'.format(x))

def firsttwo(x):
    return x[:2]

parity = lambda x: firsttwo(binary(x)).count('1') % 2