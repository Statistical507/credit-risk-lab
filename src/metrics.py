def calculate_cure_rate(defaults_accounts, cure_accounts):
    if cure_accounts > defaults_accounts or defaults_accounts == 0:
        return "valor de los parametros incorrectos"
    else:
        return cure_accounts / defaults_accounts