from typing import Dict, List, Optional, Any


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

def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по полю "date".
    Если у какой‑либо записи нет ключа "date", она отбрасывается.
    """
    # Оставляем только те элементы, где ключ "date" действительно присутствует
    filtered = [t for t in transactions if "date" in t]

    # Сортируем уже «чистый» список
    return sorted(filtered, key=lambda x: x["date"], reverse=reverse)
