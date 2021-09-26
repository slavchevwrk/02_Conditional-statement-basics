deposit = float(input())
months = int(input())
annual_rate_percentage = float(input())

annual_rate = annual_rate_percentage / 100
monthly_rate = deposit * (annual_rate / 12)

total_loan = deposit + months * monthly_rate

print(total_loan)
