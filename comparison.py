def compare_loans(loans):
    comparison = []
    for loan in loans:
        schedule = loan.amortization_schedule()
        comparison.append({
            'Principal': loan.principal,
            'Rate': loan.rate,
            'Term': loan.term_years,
            'Total Interest': total_interest(schedule),
            'APR': apr(loan)
        })
    return pd.DataFrame(comparison)