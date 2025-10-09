from typing import Dict, List, Optional


def filter_by_state(
        transactions: List[Dict],
        state: Optional[str] = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует список операций по статусу.

    :param transactions: Список словарей с данными операций
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список операций
    """
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(
        transactions: List[Dict],
        reverse: bool = True
) -> List[Dict]:
    """
    Сортирует операции по дате.

    :param transactions: Список словарей с данными операций
    :param reverse: Флаг сортировки (True — по убыванию, False — по возрастанию)
    :return: Отсортированный список операций
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
