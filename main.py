from src.portfolio import calculate_default_rate


defaults = 125
total_accounts = 5000

default_rate = calculate_default_rate(
    defaults,
    total_accounts
)

print(f"Default rate: {default_rate:.2%}")