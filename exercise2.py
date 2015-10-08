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
name_that_shape()
dict = {3:'triangle', 4:'tetragon', 5:'pentagon',6:'hexagon',7:'heptagon',8:'octagon',9:'nonagon',10:'decagon'}
guess =(raw_input('How many sides does your polygon have?'))
if (guess)=="3":
    print ('that is called a:')+ dict[3]
if guess=="4":
    print ('that is called a:')+ dict[4]
if guess=="5":
    print ('that is called a:')+ dict[5]
if guess=="6":
    print ('that is called a:')+ dict[6]
if guess=="7":
    print ('that is called a:')+ dict[7]
if guess=="8":
    print ('that is called a:')+ dict[8]
if guess=="9":
    print ('that is called a:')+ dict[9]
if guess=="10":
    print ('that is called a:')+ dict[10]
if guess>"10":
    print ('error')

# you have to be able to use the program to discern whether the input is one of the
#numbers from 1 to 10.
#if it isn't, the program should print: Error

