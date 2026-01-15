import numpy_financial as npf

def generate_schedule(loan):
    return loan.amortization_schedule()

def total_interest(schedule):
    return sum(schedule['Interest'])

def apr(loan):
    schedule = loan.amortization_schedule()
    payments = schedule['Payment']
    cashflows = [loan.principal] + [-p for p in payments]
    apr_rate = npf.irr(cashflows) * 12
    return apr_rate