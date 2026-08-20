def calculate_cure_rate(defaults_accounts, cure_accounts):
    if (
        defaults_accounts > 0
        and cure_accounts >= 0
        and cure_accounts <= defaults_accounts
    ):
        return cure_accounts / defaults_accounts

    return None