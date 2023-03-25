import requests
import numpy as np

currencies = sorted(["USD", "EUR", "UAH", "AED", "FKP", "SLL", "NOK", "CHF", "GBP", "SEK"])


def get_data(from_currency="EUR"):
    api_key = "86ac0673d4d031f252253cc4"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    return response.json()


def get_all_currencies(currencies_list):
    currencies_parsed = {currency: get_data(currency) for currency in currencies_list}
    return currencies_parsed


def build_currencies_list(data, currencies=currencies):
    temp = {name: value['conversion_rates'] for name, value in data.items()}
    for key, value in temp.items():
        temp[key] = {key: value for key, value in value.items() if key in currencies}
    return temp


def build_map(data, currencies=currencies):
    new_data = []
    for key, value in data.items():
        value = [value[currency] for currency in currencies]
        new_data.append(value)
    return new_data


def get_variants(data, left, right, amount, currencies=currencies):
    currency_id = {name: pos for pos, name in enumerate(currencies)}
    left_to_int = [x * amount for x in data[currency_id[left]]]
    int_to_right = [currency[currency_id[right]] for currency in data]
    temp = np.array(left_to_int) * int_to_right
    return left_to_int, temp, {currencies[i]: value for i, value in enumerate(temp) if currencies[i] != left}


def rev_variants(variants):
    return {value: key for key, value in variants.items()}


def get_customers_best(variants):
    variants_rev = rev_variants(variants)
    best = max(variants.values())
    return variants_rev[best]


def get_brokers_best(variants):
    variants_rev = rev_variants(variants)
    temp = {variants_rev[value]: value - np.floor(value * 100)/100 for value in variants.values()}
    max_value = list(temp.values())
    max_key = list(temp.keys())
    key = max_key[max_value.index(max(max_value))]
    return temp, {key: max(max_value)}


def get_result(left, right, amount):
    all_currencies = get_all_currencies(currencies)
    conversions = build_currencies_list(all_currencies)
    currencies_map = build_map(conversions, currencies)
    left_to, to_right, variants = get_variants(currencies_map, left=left, right=right, amount=amount)
    first_step = {currencies[i]: value for i, value in enumerate(left_to) if currencies[i] != left}
    second_step = {currencies[i]: value for i, value in enumerate(to_right) if currencies[i] != left}
    customers_best = get_customers_best(variants)
    brokers_margins, brokers_best = get_brokers_best(variants)
    return {'variants': variants, 'first_step': first_step, 'second_step': second_step,
            'customers_best': customers_best, 'brokers_margins': brokers_margins, 'brokers_best': brokers_best,
            'from_currency': left, 'to_currency': right}

