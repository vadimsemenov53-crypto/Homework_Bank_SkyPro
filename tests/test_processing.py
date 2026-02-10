import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_base(processing):
    assert filter_by_state(processing) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
    assert filter_by_state(processing, state="CANCELED") == [
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    ]


def test_filter_by_state_wrong_type():
    with pytest.raises(AttributeError):
        filter_by_state([123356])
    with pytest.raises(AttributeError):
        filter_by_state(["error"])


def test_filter_by_state_not_key():
    assert filter_by_state(
            [
                {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            ]
        ) == []


@pytest.mark.parametrize(
    "my_list, expected",
    [
        (
            [
                {"state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"date": "2019-07-03T18:35:29.512364", "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "state": "CANCELED"},
            ],
        ),
        (
            [{"id": 594226727, "state": "CANCELED"}, {"id": 615064591, "state": "CANCELED"}],
            [{"id": 594226727, "state": "CANCELED"}, {"id": 615064591, "state": "CANCELED"}],
        ),
    ],
)
def test_filter_by_state_another_list(my_list, expected):
    assert filter_by_state(my_list, state="CANCELED") == expected


def test_sort_by_date_base(processing):
    assert sort_by_date(processing) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]

    assert sort_by_date(processing, sort=False) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


def test_sort_by_date_another_date():
    assert sort_by_date(
        [
            {"date": "2032-01-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            {"date": "1900-02-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        ],
        sort=False,
    ) == [
        {"date": "1900-02-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2032-01-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


def test_sort_by_date_not_key():
    with pytest.raises(KeyError):
        sort_by_date([{"id": 594226727, "state": "CANCELED"}, {"id": 615064591, "state": "CANCELED"}])
