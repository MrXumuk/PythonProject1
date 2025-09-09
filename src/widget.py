from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(data: str) -> str:
    """Основная функция маскировки карт и счетов"""
    parts = data.rsplit(' ', 1)

    if len(parts) != 2:
        return data

    name, number = parts
    number = number.strip()

    try:
        if "Счет" in name:
            masked = get_mask_account(number)
        else:
            masked = get_mask_card_number(number)
    except ValueError:
        return data  # Возвращаем исходные данные при ошибке

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """Форматирует дату из ISO-формата в DD.MM.YYYY"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return "Неверный формат даты"
