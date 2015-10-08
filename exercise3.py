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

    Inputs: yes, no

    Expected Outputs:
    -Is the car silent when you enter the key?
    -Are the battery terminals corroded?
    -Clean the terminals and try starting the car again
    -Replace the cables and try again
    -Does the car make a clicking noise?
    -Does the car crank up but fail to start?
    -Check spark plug connections
    -Does the engine start then die?
    -Does your car have fuel injection?
    -Get it in for service
    -Check to ensure the choke is opening and closing

    Errors:

    """



print "Automated Car Diagnostic. Enter yes or no to diagnose problem:"

carSilent = raw_input(("Is the car silent when you enter the key?"))
if carSilent== 'yes':
   batteries_corroded = (raw_input("Are the battery terminals corroded?"))
   if batteries_corroded=='yes':
    print ('Clean the terminals and try starting the car again.')
   if batteries_corroded=='no':
    print ('Replace the cables and try again')
if carSilent== 'no':
    clicking_noise = (raw_input("Does the car make a clicking noise"))
    if clicking_noise=='yes':
        print ('Replace the battery')
    if clicking_noise=='no':
        start_fail = (raw_input("Does the car crank up but fail to start?"))
        if start_fail=='yes':
            print ('Check spark plug connections')
        if start_fail=='no':
            engine_fail = (raw_input("Does the engine start then die?"))
            if engine_fail=='yes':
                fuel_injection = (raw_input("Does your car have fuel injection"))
                if fuel_injection=='yes':
                    print('Get it in for service')
                if fuel_injection=='no':
                    print ('Check to ensure the choke is opening and closing')