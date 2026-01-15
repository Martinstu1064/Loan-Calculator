import pandas as pd
from loan import FixedRateLoan
from amortization import total_interest

def prepayment_scenario(loan, extra_payment):
    df = loan.amortization_schedule()
    balance = loan.principal
    schedule = []
    for i, row in df.iterrows():
        interest = balance * loan.rate/12
        principal = row['Payment'] - interest + extra_payment
        balance -= principal
        schedule.append({'Month': i+1, 'Payment': row['Payment'] + extra_payment,
                         'Principal': principal, 'Interest': interest,
                         'Balance': max(balance,0)})
        if balance <= 0:
            break
    return pd.DataFrame(schedule)

def refinancing_break_even(old_loan, new_rate, new_term):
    old_total_interest = total_interest(old_loan.amortization_schedule())
    new_loan = FixedRateLoan(old_loan.principal, new_rate, new_term)
    new_total_interest = total_interest(new_loan.amortization_schedule())
    savings = old_total_interest - new_total_interest
    return savings
