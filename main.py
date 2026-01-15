from loan import FixedRateLoan
from amortization import generate_schedule, total_interest, apr
from analysis import prepayment_scenario
from affordability import affordability

# fixed-rate loan
loan1 = FixedRateLoan(principal=100000, rate=0.05, term_years=20)
schedule = generate_schedule(loan1)
print(schedule.head())
print("Total interest:", total_interest(schedule))
print("APR:", apr(loan1))

# Prepayment scenario
prepay_schedule = prepayment_scenario(loan1, extra_payment=200)
print(prepay_schedule.head())

# Affordability
max_payment = affordability(income=5000, debts=1000)
print("Max affordable payment:", max_payment)
