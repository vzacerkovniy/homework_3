from src.processing import filter_by_state, sort_by_date

# Тесты с использованием фикстур


# Для filter_by_state
def test_filter_by_state(list_executed: list) -> None:
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
        == list_executed
    )


def test_filter_by_state_1(list_canceled: list) -> None:
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="CANCELED",
        )
        == list_canceled
    )


def test_filter_by_state_2(list_empty: list) -> None:
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
        == list_empty
    )


def test_filter_by_state_3(list_executed: list) -> None:
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="PUPUPU",
        )
        == list_executed
    )


# Для sort_by_date
def test_sort_by_date(sorted_up: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            ascending=False,
        )
        == sorted_up
    )


def test_sort_by_date_1(sorted_down: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            ascending=True,
        )
        == sorted_down
    )


def test_sort_by_date_2(sorted_up_1: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            ascending=False,
        )
        == sorted_up_1
    )


def test_sort_by_date_3(sorted_up_2: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "bebebe"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "123332"},
            ],
            ascending=False,
        )
        == sorted_up_2
    )
