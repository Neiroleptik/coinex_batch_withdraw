# Скрипт для вывода средств с CoinEx

Этот скрипт предназначен для автоматизации вывода средств с CoinEx на множество адресов.
## Требования

- Python 3.9
- Аккаунт CoinEx
- Адреса кошельков, добавленные в белый список на CoinEx
- Ради блага всего человечества, советую использовать PyCharm Community Edition

## Установка

1. Скачайте этот репозиторий.
2. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Настройка

1. Добавьте адреса кошельков в файл `wallets.txt`, по одному на каждую строку.

2. Получите ваш API-ключ и секрет с CoinEx:
   - Перейдите на страницу управления API https://www.coinex.com/ru/apikey.
   - Создайте новый API-ключ или используйте существующий.
   - Обязательно добавьте ваш IP-адрес в белый список для разрешения выводов.

3. Добавьте ваши адреса кошельков в белый список на CoinEx:
   - На странице управления API выберите "Добавить Партию" для загрузки списка адресов кошельков.

4. Введите ваши ACCESS_ID, SECRET_KEY в main.py


## Конфигурация

Откройте файл скрипта и обновите следующие переменные:

- `ACCESS_ID`: Ваш ACCESS_ID CoinEx.
- `SECRET_KEY`: Ваш SECRET_KEY CoinEx.
- `symbolWithdraw`: Монета, которую вы хотите вывести (например, 'SOL').
- `network`: Сеть для вывода (например, 'SOL').
- `AMOUNT_FROM`: Минимальная сумма для вывода.
- `AMOUNT_TO`: Максимальная сумма для вывода.

## Использование

Запустите скрипт:

```bash
python main.py
```

## Описание скрипта

Скрипт читает адреса кошельков из файла `wallets.txt` и выполняет вывод средств на каждый адрес с случайной суммой в диапазоне от `AMOUNT_FROM` до `AMOUNT_TO` и со случайной задержкой между выводами.

## Автор
- [github](https://github.com/Neiroleptik)
- [Telegram](https://t.me/jero1n)
- Полное описание скрипта: [Still Early Telegram](https://t.me/Still_Early/1033)
