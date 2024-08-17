from src.masks import get_mask_account, get_mask_card_number

# Тесты с использованием фикстур


# Для get_mask_card_number
def test_get_mask_card_number(num_usual: str) -> None:
    assert get_mask_card_number("Карта 1111 1111 1111 1111") == num_usual


def test_get_mask_card_number_1(num_usual: str) -> None:
    assert get_mask_card_number("Карта1111111111111111") == num_usual


def test_get_mask_card_number_2(num_visa: str) -> None:
    assert get_mask_card_number("Visa 1111 1111 1111 1111") == num_visa


def test_get_mask_card_number_3(num_invalid: str) -> None:
    assert get_mask_card_number("1111 1111 1111 1111") == num_invalid


def test_get_mask_card_number_4(num_invalid: str) -> None:
    assert get_mask_card_number("Карта 1111 1111 1111") == num_invalid


def test_get_mask_card_number_5(num_invalid: str) -> None:
    assert get_mask_card_number("Карта 1111 1111 1111 1111 1111") == num_invalid


def test_get_mask_card_number_6(num_invalid: str) -> None:
    assert get_mask_card_number("") == num_invalid


def test_get_mask_card_number_7(num_invalid: str) -> None:
    assert get_mask_card_number("Carl Jonson") == num_invalid


# Для get_mask_account
def test_get_mask_account(account_usual: str) -> None:
    assert get_mask_account("Счет 11111111111111111111") == account_usual


def test_get_mask_account_1(account_usual: str) -> None:
    assert get_mask_account("Счет11111111111111111111") == account_usual


def test_get_mask_account_2(account_invalid: str) -> None:
    assert get_mask_account("Peppa") == account_invalid


def test_get_mask_account_3(account_invalid: str) -> None:
    assert get_mask_account("11111111111111111111") == account_invalid


def test_get_mask_account_4(account_invalid: str) -> None:
    assert get_mask_account("Счет 111") == account_invalid


def test_get_mask_account_5(account_invalid: str) -> None:
    assert get_mask_account("Счет 123456789123456789123456789") == account_invalid


def test_get_mask_account_6(account_invalid: str) -> None:
    assert get_mask_account("") == account_invalid
