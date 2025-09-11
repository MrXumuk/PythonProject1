from src import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("") == "Некорректный номер карты"


def test_get_mask_account():
    assert get_mask_account("73654116830135873705") == "**3705"
    assert get_mask_account("123") == "Некорректный номер счета"
