from typing import List, Dict, Optional


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
