import time
import requests
import hmac
import hashlib
import json
import random
from termcolor import cprint

def coinex_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, ACCESS_ID, SECRET_KEY, withdraw_method="on_chain"):
    url = "https://api.coinex.com/v2/assets/withdraw"
    timestamp = str(int(time.time() * 1000))

    params = {
        "amount": str(amount_to_withdrawal),
        "ccy": symbolWithdraw,
        "to_address": address,
        "withdraw_method": withdraw_method
    }
    if network:
        params["chain"] = network


    body = json.dumps(params)
    print(body)
    prepared_str = "POST"+"/v2/assets/withdraw"+f"{body}{timestamp}"
    signature = hmac.new(bytes(SECRET_KEY, 'latin-1'), msg=bytes(prepared_str, 'latin-1'), digestmod=hashlib.sha256).hexdigest().lower()

    headers = {
        'X-COINEX-KEY': ACCESS_ID,
        'X-COINEX-SIGN': signature,
        'X-COINEX-TIMESTAMP': timestamp,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=body)
        print(response)
        response_data = response.json()
        if response_data['code'] == 0:
            cprint(f">>> Успешно | {address} | {amount_to_withdrawal}", "green")
        else:
            cprint(f">>> Неудачно | {address} | ошибка : {response_data['message']}", "red")
    except Exception as error:
        cprint(f">>> Неудачно | {address} | ошибка : {error}", "red")

# P.S. Не забудьте добавить кошельки в whitelist >_<
if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    symbolWithdraw = 'SOL'
    network = 'SOL'

    # CoinEx api_keys here
    ACCESS_ID = "access_id"
    SECRET_KEY = "secret_key"
    AMOUNT_FROM = 0.02
    AMOUNT_TO = 0.03

    cprint('\a\n/// start withdrawing...', 'white')
    for wallet in wallets_list:
        num_of_f = random.randint(3, 8)
        amount_to_withdrawal = round(random.uniform(AMOUNT_FROM, AMOUNT_TO), num_of_f)
        coinex_withdraw(wallet, amount_to_withdrawal, symbolWithdraw, network, ACCESS_ID, SECRET_KEY)
        time.sleep(random.randint(10, 30))
