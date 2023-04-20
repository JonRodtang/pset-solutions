'''
6.0001 Fall 2016 ps1c
Intro to Computer Science and Programming in Python
Jon Rodtang
jonmro@pvv.ntnu.no
'''

# User inputs
annual_salary   = float(input("Enter the starting salary: "))

current_savings      = 0
savings_rate         = 1.0
steps_bisection      = 0
saving_time          = 36           # months  
total_cost           = 1000000
semi_annual_raise    = 0.07
portion_down_payment = 0.25
r                    = 0.04         # annual returns
down_payment_cost = total_cost * portion_down_payment 
monthly_contribution = (annual_salary / 12) * savings_rate


for _ in range(saving_time):
    monthly_returns = current_savings * (r / 12) 
    current_savings += monthly_returns + monthly_contribution
if current_savings < down_payment_cost:
            print("It is not possible to pay the down payment in three years.")
            exit(0)



upper = 10000
lower = 0
found = False
while not found:
    savings_rate = ((upper + lower) // 2) / 10000 
    current_savings      = 0
    monthly_contribution = (annual_salary / 12) * savings_rate
    steps_bisection     += 1
    for _ in range(saving_time):
        monthly_returns = current_savings * (r / 12) 
        current_savings += monthly_returns + monthly_contribution
    if (down_payment_cost - 100) <= current_savings <= (down_payment_cost + 100):
        found = True
    elif current_savings < down_payment_cost:
        lower = (upper + lower) // 2
    elif current_savings > down_payment_cost:
        upper = (upper + lower) // 2

print("Best savings rate:", savings_rate)
print("Steps in bisection search:", steps_bisection)
