from src.portfolio import calculate_default_rate
from src.metrics import calculate_cure_rate


defaults = 125
total_accounts = 5000

default_rate = calculate_default_rate(
    defaults,
    total_accounts
)

print(f"Default rate: {default_rate:.2%}")

defaults = 0
cure_accounts = 0

cure_rate = calculate_cure_rate(
    defaults,
    cure_accounts
)

print(f"Cure rate: {cure_rate}")