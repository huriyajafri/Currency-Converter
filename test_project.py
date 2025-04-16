from project import convert_currency, get_exchange_rate, get_available_currencies, validate_input

def main():
    test_convert_currency()
    test_get_exchange_rate()
    test_get_available_currencies()
    test_validate_input()


def test_convert_currency():
    assert convert_currency(100, "USD", "EUR") == 92.70
    assert convert_currency(100, "EUR", "USD") == 108.00


def test_validate_input():
    assert validate_input('100', 'USD', 'EUR') == (True, "")
    assert validate_input('-100', 'USD','EUR') == (False, "Please enter a valid number greater than zero.")
    assert validate_input('abc', 'USD','EUR') == (False, "Please enter a valid amount.")
    assert validate_input('100', 'XYZ','EUR') == (False, "Please select a valid currency.")
    assert validate_input('100', 'USD','EU') == (False, "Please select a valid currency.")
    assert validate_input('100', 'USD','pkr') == (False, "Please select a valid currency.")


def test_get_available_currencies():
    currencies = get_available_currencies()
    assert 'EUR' in currencies, "EUR should be in the list of available currencies"
    assert 'USD' in currencies, "USD should be in the list of available currencies"
    assert 'PK' not in currencies, "PK should not be in the list of available currencies"

def test_get_exchange_rate():
    rate = get_exchange_rate('USD', 'EUR')
    assert rate > 0

if __name__ == "__main__":
    main()
