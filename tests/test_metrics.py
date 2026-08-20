from src.metrics import calculate_cure_rate

def test_cure_rate_normal():
    defaults_accounts = 100
    cure_accounts = 30
    
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate == 0.3

def test_cure_rate_zero_cures():
    defaults_accounts = 100
    cure_accounts = 0
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate == 0

def test_cure_rate_full_cure():
    defaults_accounts = 100
    cure_accounts = 100
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate == 1

def test_cure_rate_cures_greater_than_defaults():
    defaults_accounts = 100
    cure_accounts = 101
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate is None

def test_cure_rate_zero_defaults():
    defaults_accounts = 0
    cure_accounts = 0
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate is None

def test_cure_rate_positive_cures_zero_defaults():
    defaults_accounts = 0
    cure_accounts = 10
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate is None

def test_cure_rate_negative_cures():
    defaults_accounts = -10
    cure_accounts = 5
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate is None

def test_cure_rate_negative_defaults():
    defaults_accounts = 10
    cure_accounts = -5
    cure_rate = calculate_cure_rate(
        defaults_accounts,
        cure_accounts
    )
    assert cure_rate is None
