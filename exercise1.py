#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


__author__ = 'SebsMacBook'
#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion
This module prints the amount of money that Lakshmi has remaining
after the stock transactions
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"
#just a preliminary attempt at wrapping my head around this..
#I don't think Im very good at this...   ...yet...
sharePrice = raw_input('How much did Lakshmi pay per share?')
brokerCost = raw_input('What percentage did she pay her broker?')
print ('commission per share:')
print (float(sharePrice)*0.03)
shareQuantity = raw_input('How many shares did Lakshmi buy?')
totalCost = (float(sharePrice)*float(shareQuantity))
commissionPaid = (float(sharePrice)*float(shareQuantity))*0.03
moneyLeft = (float(totalCost-commissionPaid))
print ('total cost =')+ str(totalCost)
#print (float(sharePrice)*float(shareQuantity))
print ('This means Lakshmi paid her broker a total of:')
print commissionPaid
print ('This leaves Lakshmi with:')
print moneyLeft