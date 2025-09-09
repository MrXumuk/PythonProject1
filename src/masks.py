def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты. Оставляет первые 4 и последние 4 цифры."""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен быть 16-значным числом")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета. Оставляет последние 4 цифры."""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Счет должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
