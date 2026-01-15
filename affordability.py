def affordability(income, debts, max_ratio=0.4):
    available = income * max_ratio - debts
    return max(available, 0)