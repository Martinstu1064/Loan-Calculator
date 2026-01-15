import pandas as pd
from datetime import datetime

class Loan:
    def __init__(self, principal, rate, term_years, start_date=datetime.today()):
        self.principal = principal
        self.rate = rate
        self.term_years = term_years
        self.start_date = start_date

    def monthly_payment(self):
        n = self.term_years * 12
        r = self.rate / 12
        return self.principal * r / (1 - (1 + r) ** -n)

class FixedRateLoan(Loan):
    def amortization_schedule(self):
        n = self.term_years * 12
        r = self.rate / 12
        balance = self.principal
        schedule = []
        for i in range(1, n+1):
            interest = balance * r
            principal = self.monthly_payment() - interest
            balance -= principal
            schedule.append({
                'Month': i,
                'Payment': self.monthly_payment(),
                'Principal': principal,
                'Interest': interest,
                'Balance': max(balance, 0)
            })
        return pd.DataFrame(schedule)
