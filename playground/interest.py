# def compound_interest(principal, interest_rate, time):
#     return principal * (1 + interest_rate)**time

# principal_amount = 2500  
# annual_interest_rate = 0.04 
# daily_interest_rate = annual_interest_rate / 365  
# days_in_year = 365

# print(f"{'Day':<5} {'Amount':<10}")

# for day in range(1, days_in_year + 1):
#     amount_after_day = compound_interest(principal_amount, daily_interest_rate, day)
#     print(f"{day:<5} {amount_after_day:.2f}")


# def compound_interest_daily(principal, annual_interest_rate, days):
#     daily_interest_rate = annual_interest_rate / 365
#     return principal * (1 + daily_interest_rate)**days

# principal_amount = 2500  # Initial principal amount
# annual_interest_rate = 0.04  # Annual interest rate (4%)
# days_in_year = 365  # Number of days in a year

# print(f"{'Day':<5} {'Amount':<10}")

# for day in range(1, days_in_year + 1):
#     amount_after_day = compound_interest_daily(principal_amount, annual_interest_rate, day)
#     print(f"{day:<5} {amount_after_day:.2f}")
