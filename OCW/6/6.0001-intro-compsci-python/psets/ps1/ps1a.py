'''
6.0001 Fall 2016 ps1a
Intro to Computer Science and Programming in Python
Jon Rodtang
jonmro@pvv.ntnu.no
'''

import math
# User inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost    = float(input("Enter the cost of your dream home: "))

current_savings = 0
portion_down_payment = 0.25

# annual returns
r = 0.04

down_payment_cost = total_cost * portion_down_payment
monthly_contribution = (annual_salary / 12) * portion_saved


months = 0

while current_savings < down_payment_cost:
    months += 1       
    monthly_returns = current_savings * (r / 12) 
    current_savings += monthly_returns + monthly_contribution

print("Number of months:", months)

