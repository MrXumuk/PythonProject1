import pytest

from typing import List, Dict, Any
from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state():
    """Тестирование функции filter_by_state"""

    # Подготовка тестовых данных
    test_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELED"},
        {"id": 5, "state": "EXECUTED"},
    ]

    # Тестирование с корректным значением состояния
    expected_executed = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 5, "state": "EXECUTED"},
    ]
    assert filter_by_state(test_data, "EXECUTED") == expected_executed

    # Тестирование с другим состоянием
    expected_pending = [
        {"id": 2, "state": "PENDING"},
    ]
    assert filter_by_state(test_data, "PENDING") == expected_pending

    # Тестирование с состоянием, которого нет в данных
    expected_empty = []
    assert filter_by_state(test_data, "UNKNOWN") == expected_empty

    # Тестирование с состоянием по умолчанию (EXECUTED)
    assert filter_by_state(test_data) == expected_executed


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура для создания тестовых данных."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-05-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2024-05-03T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-05-02T14:00:00"},
    ]


def test_sort_by_date_descending(sample_data: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по убыванию."""
    sorted_data = sort_by_date(sample_data, reverse=True)
    assert [item["id"] for item in sorted_data] == [2, 3, 1]


def test_sort_by_date_ascending(sample_data: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по возрастанию."""
    sorted_data = sort_by_date(sample_data, reverse=False)
    assert [item["id"] for item in sorted_data] == [1, 3, 2]


def test_sort_by_date_empty_list() -> None:
    """Тестирование с пустым списком."""
    assert sort_by_date([]) == []


def test_sort_by_date_missing_date_key() -> None:
    """Тестирование с отсутствующим ключом 'date'."""
    data_missing_date = [{"id": 1, "state": "EXECUTED"}]
    assert sort_by_date(data_missing_date) == []


# Запускаем тесты, если файл выполняется как основной
if __name__ == "__main__":
    pytest.main()