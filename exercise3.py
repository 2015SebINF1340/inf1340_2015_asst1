#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
    car_silent = (raw_input("Is the car silent when you enter the key?"))
    batteries_corroded = (raw_input("Are the battery terminals corroded?"))
    clicking_noise = (raw_input("Does the car crank up but fail to start?"))
    engine_start = (raw_input("Does the engine start and then die?"))
    fuel_injection = (raw_input("Does you car have fuel injection"))

    if car_silent == "y":
        print(batteries_corroded)
            if batteries_corroded == "y":
                print("Clean terminals and try starting again.")
        else:
            print("Replace cables")



diagnose_car()


diagnose_car()