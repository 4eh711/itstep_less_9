import requests
from bs4 import BeautifulSoup

# Клас для отримання курсів валют і конвертації валют
class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    # Отримання актуальних курсів валют з сайту Національного банку України
    def update_rates(self):
        url = 'https://bank.gov.ua/'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            currency_block = soup.find('div', class_='exchange-rate')

            # Знайдемо курс долара США
            usd_rate_row = currency_block.find('td', text='Долар США')
            usd_rate = usd_rate_row.find_next('td').text.strip()

            # Оновимо курс долара США у внутрішньому словнику
            self.rates['USD'] = float(usd_rate)

    # Конвертація суми з однієї валюти в іншу
    def convert(self, amount, from_currency, to_currency):
        if from_currency != 'UAH':
            amount = amount / self.rates[from_currency]
        converted_amount = amount * self.rates[to_currency]
        return converted_amount

# Створення екземпляра класу CurrencyConverter
converter = CurrencyConverter()

# Оновлення курсів валют
converter.update_rates()

# Виведення курсу долара США
print(f'Курс долара США: {converter.rates["USD"]} UAH')

# Приклад конвертації суми з доларів США в євро
usd_amount = 100
converted_amount = converter.convert(usd_amount, 'USD', 'EUR')
print(f'{usd_amount} USD = {converted_amount:.2f} EUR')