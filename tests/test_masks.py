import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        (" 1234567890123456 ", "1234 56** **** 3456"),  # пробелы вокруг
    ]
)


def test_get_mask_card_number_success(raw_input: str, expected: str) -> None:
    """
    Проверяем корректную маскировку номера карты.
    Функция должна работать и если в строке есть пробелы их мы удаляем перед передачей в функцию.
    """
    cleaned = raw_input.replace(" ", "")
    assert get_mask_card_number(cleaned) == expected


@pytest.mark.parametrize(
    "bad_input, message",
    [
        ("123456789012345", "Номер карты должен быть 16-значным числом"),
        ("12345601234567", "Номер карты должен быть 16-значным числом"),
        ("1234abcd9012efgh", "Номер карты должен быть 16-значным числом"),
        ("", "Номер карты должен быть 16-значным числом"),
    ],
)
def test_get_mask_card_number_errors(bad_input: str, message: str) -> None:
    """Проверяем, при неверных данных бросается ValueError."""
    cleaned = bad_input.replace(" ", "")
    with pytest.raises(ValueError) as exc:
        get_mask_card_number(cleaned)
    assert str(exc.value) == message


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        ("12345678901234567890", "**7890"),
        ("1234 5678 90123456 7890", "**7890"),
        ("  9876543210  ", "**3210"),
        ("0000", "**0000"),
    ],
)
def test_get_mask_account_success(raw_input: str, expected: str) -> None:
    """Корректная работа маскировки счета."""
    cleaned = raw_input.replace(" ", "")
    assert get_mask_account(cleaned) == expected


@pytest.mark.parametrize(
    "bad_input, message",
    [
        ("123", "Счет должен содержать минимум 4 цифры"),   # менее 4 цифр
        ("12ab34", "Счет должен содержать минимум 4 цифры"),# буквы
        ("", "Счет должен содержать минимум 4 цифры"),
    ],
)
def test_get_mask_account_errors(bad_input: str, message: str) -> None:
    """Провер, что функция бросает ValueError при неправильных данных."""
    cleaned = bad_input.replace(" ", "")
    with pytest.raises(ValueError) as exc:
        get_mask_account(cleaned)
    assert str(exc.value) == message


if __name__ == "__main__":
    pytest.main([__file__])