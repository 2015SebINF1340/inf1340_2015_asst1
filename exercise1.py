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


"""
Calculate amount Lakshmi had left after selling her stock and paying her broker's commission,
returns if Lakshmi made a profit or loss

Inputs:
-number shares = 2000,
-price share = 900,
-price share sold = 942.75,
-broker's commission = 3%

Expected outputs:
-Remainder (amount Lakshmi had left after selling the stock and paying the broker)
-"Lakshmi made a profit"
-"Lakshmi lost money"

"""


number_share = 2000.0
price_share = 900.0
cost_share = (number_share * price_share)
broker_commission = .03 * (number_share * price_share)
bought_total = cost_share + broker_commission

number_share_sold = 2000.0
price_share_sold = 942.75
cost_share_sold = (number_share_sold * price_share_sold)
broker_commission_sold = .03 * (number_share_sold * price_share_sold)
sold_total = cost_share_sold + broker_commission_sold

sold_stock = cost_share_sold - cost_share
remainder = sold_stock - (broker_commission_sold + broker_commission)

print(remainder)
if remainder > 0.0:
    print("Lakshmi made a profit")
else:
    print("Lakshmi lost money")


