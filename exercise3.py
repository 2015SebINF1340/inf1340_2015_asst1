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

    Inputs: Y, N

    Expected Outputs:
    -Is the car silent when you turn the key?
    -Are the battery terminals corroded?
    -Clean terminals and try starting again.
    -Replace cables and try again.
    -Does the car make a clicking noise?
    -Does the car crank up but fail to start?
    -Check spark plug connections.
    -Does the engine start and then die?
    -Does your car have fuel injection?
    -Get it in for service.
    -Check to ensure the choke is opening and closing.

    Errors: Unexpected inputs (e.g. "Yes" or "No") will result in an error message

    """


    carSilent = raw_input(("Is the car silent when you enter the key?"))
    if carSilent== 'Y':
       batteries_corroded = (raw_input("Are the battery terminals corroded?"))
       if batteries_corroded=='Y':
        print ('Clean terminals and try starting again.')
       if batteries_corroded=='N':
        print ('Replace cables and try again.')
    if carSilent== 'N':
        clicking_noise = (raw_input("Does the car make a clicking noise"))
        if clicking_noise=='Y':
            print ('Replace the battery.')
        if clicking_noise=='N':
            start_fail = (raw_input("Does the car crank up but fail to start?"))
            if start_fail=='Y':
                print ('Check spark plug connections.')
            if start_fail=='N':
                engine_fail = (raw_input("Does the engine start then die?"))
                if engine_fail=='Y':
                    fuel_injection = (raw_input("Does your car have fuel injection"))
                    if fuel_injection=='Y':
                        print('Get it in for service.')
                    if fuel_injection=='N':
                        print ('Check to ensure the choke is opening and closing.')
                if engine_fail == 'N':
                    print('Engine is not getting enough fuel. Clean fuel pump.')