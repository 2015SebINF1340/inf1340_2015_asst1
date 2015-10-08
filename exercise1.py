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
money = 1000.00
print(money)

#Input the number of shares bought
#Input the cost of each share
#Calculate the total stock bought
#Calculate the stock broker's commission
#Calculate the total bought

number_share = 2000.0
price_share = 900.0
cost_share = (number_share * price_share)
broker_commission = .03 * (number_share * price_share)
bought_total = cost_share + broker_commission

#print(cost_share)
#print(broker_commission)
#print(bought_total)

#Input the number of shares sold
#Input the price of each share sold
#Calculate the stockbroker's commission

number_share_sold = 2000.0
price_share_sold = 942.75
cost_share_sold = (number_share_sold * price_share_sold)
broker_commission_sold = .03 * (number_share_sold * price_share_sold)
sold_total = cost_share_sold + broker_commission_sold

#print(cost_share_sold)
#print(broker_commission_sold)
#print(sold_total)

#Calculate amount Lakshmi had left after selling and paying the broker
sold_stock = cost_share_sold - cost_share
remainder = sold_stock - (broker_commission_sold + broker_commission)
print(remainder)

if remainder > 0.0:
    print("Lakshmi made a profit")
else:
    print("Lakshmi lost money")


