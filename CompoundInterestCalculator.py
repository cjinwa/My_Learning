start_year = int(input("enter start year\n"))
end_year = int(input("enter end year\n"))
initial_investment = int(input("enter amount to invest\n"))
stock_dividend = int(input("enter stock dividend\n"))
annual_addition = int(input("enter annual addition amount\n"))

total_years = end_year - start_year
total_amount = initial_investment

for add in range(total_years):
    total_amount += total_amount * (stock_dividend/100) + annual_addition

print(f"your total amount by {end_year} will be {total_amount:.2f}")