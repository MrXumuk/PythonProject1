# Проект "Банковские операции"

## Цель
Анализ и обработка данных о банковских операциях.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MrXumuk/PythonProject1.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Разработка
Для разработки и проверки кода рекомендуется установить следующие инструменты:
   ```shell
      poetry install --with lint
   ```

## Тестирование:
1. test_masks.py - тестируем `get_mask_account, get_mask_card_number`
2. test_widget.py - тестируем `mask_account_card, get_date`
3. test_processing.py - тестируем `filter_by_state, sort_by_date`


### Установка теста:
Установка через Poetry:
```poetry add --group dev pytest```

Установка pytest-cov:
```poetry add --group dev pytest-cov```
- Метрика, показывает на сколько процентов был протестирован код программы.

### Запуск тестов:

1. Команды, чтобы запустить тесты с оценкой покрытия:

- ```pytest``` - запуск всех тестов.
- ```pytest --cov``` — при активированном виртуальном окружении.
- ```poetry run pytest --cov``` — через poetry.


## Документация
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия
Проект распространяется под [лицензией MIT](LICENSE).