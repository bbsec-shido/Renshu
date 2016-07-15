#!python
"""
rensyu
by bbsec-shido
"""
import sys

def rensyu(name="World"):
    return "Hello {}".formate(name)

if __name__=='__main__':
    print(rensyu(sys.argv[1]))
