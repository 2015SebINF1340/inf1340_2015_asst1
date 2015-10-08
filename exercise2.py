#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3, 4, 5, 6, 7, 8, 9, 10 and any number >10

    Expected Outputs: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon and error

    Errors: numbers >10 will result in an error message.

    """
#decided to add the values to a dictionary

    dict = {3:'triangle', 4:'quadrilateral', 5:'pentagon',6:'hexagon',7:'heptagon',8:'octagon',9:'nonagon',10:'decagon'}
    guess = (raw_input('How many sides does your polygon have?'))
    if (guess)=="3":
        print dict[3]
    elif (guess)=="4":
        print dict[4]
    elif (guess)=="5":
        print dict[5]
    elif (guess)=="6":
        print dict[6]
    elif (guess)=="7":
        print dict[7]
    elif (guess)=="8":
        print dict[8]
    elif (guess)=="9":
        print dict[9]
    elif (guess)=="10":
        print dict[10]
    else:
        print ('Error')


# name_that_shape()
# you have to be able to use the program to discern whether the input is one of the
#numbers from 1 to 10.
#if it isn't, the program should print: Error

