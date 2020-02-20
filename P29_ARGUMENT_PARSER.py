#Author: VEDANT GHODKE
#In this example w will see the example for Python argument parser

import argparse

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--VEDANT', help = 'VEDANT GHODKE', action = 'store_true')
    arg = parser.parse_args()
    if(arg.VEDANT):
        VEDANT()
    else:
        print('Please add some arguments. Type ArgumentParser -h for more details')


def VEDANT():
    print('VEDANT GHODKE')


if __name__ == '__main__':
    argumentParser()