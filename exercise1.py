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
#I became obsessed with having an interactive program
#The first section is intended to calculate:
# the full cost of 2000 shares at 900 each and how much commission was paid
sharePrice = raw_input('How much did Lakshmi pay per share?')
brokerCost = raw_input('What percentage did she pay her broker?')
print ('commission per share:')
print (float(sharePrice)*0.03)
shareQuantity = raw_input('How many shares did Lakshmi buy?')
print ('total amount paid for shares:')
print (float(sharePrice)*float(shareQuantity))
commissionPaid = (float(sharePrice)*float(shareQuantity))*0.03
print ("Stockbrocker's commission")
print (commissionPaid)
print ('total cost:')
print ((float(sharePrice)*float(shareQuantity)+commissionPaid))
#this second section uses the same calculations to determine
#the totals of Lakshmi's sales
shareSalePrice = raw_input('How much did Lakshmi sell her shares for?')
newBrokerCost = raw_input('What percentage did she pay her broker?')
print ('commission per share:')
print (float(shareSalePrice)*0.03)
shareSaleQuantity = raw_input('How many shares did Lakshmi sell?')
print ('total amount paid for shares:')
print (float(shareSalePrice)*float(shareSaleQuantity))
saleCommissionPaid = (float(shareSalePrice)*float(shareSaleQuantity))*0.03
print ("Stockbrocker's commision")
print (saleCommissionPaid)

print ("total cost:")
print ((float(shareSalePrice)*float(shareSaleQuantity))+(saleCommissionPaid))
moneyLeft = ((float(sharePrice)*float(shareQuantity)+commissionPaid))\
-((float(shareSalePrice)*float(shareSaleQuantity))+(saleCommissionPaid))
print ('Did Lakshmi make any money?')
if moneyLeft>=0.0:
    print ('Looks like Lakshmi made money')
else:
    print ('Looks like Lakshmi lost money')


