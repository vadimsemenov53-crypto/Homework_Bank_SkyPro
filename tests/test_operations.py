import pytest

from src.operations import count_operations_by_category, filter_operations_by_description


def test_filter_operations_by_description_base(operations_for_re_collections):
    assert filter_operations_by_description(operations_for_re_collections, "Открытие вклада") == [
        {
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "id": 587085106,
            "operationAmount": {"amount": "48223.05", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_filter_operations_by_description_non_search(operations_for_re_collections):
    assert filter_operations_by_description(operations_for_re_collections, "") == []
    assert filter_operations_by_description(operations_for_re_collections, "qwerty") == []


def test_filter_operations_by_description_wrong_type(operations_for_re_collections):
    with pytest.raises(TypeError):
        filter_operations_by_description(operations_for_re_collections, 133)
    with pytest.raises(AttributeError):
        filter_operations_by_description({"description": "Открытие вклада"}, "Открытие вклада")


def test_count_operations_by_category_base(operations_for_re_collections, categories_for_re_collections):
    assert count_operations_by_category(operations_for_re_collections, categories_for_re_collections) == {
        "Открытие вклада": 1,
        "Перевод организации": 3,
        "Перевод с карты на счет": 2,
    }
    assert count_operations_by_category(operations_for_re_collections, ["Открытие вклада"]) == {"Открытие вклада": 1}


def test_count_operations_by_category_non_categories(operations_for_re_collections):
    assert count_operations_by_category(operations_for_re_collections, []) == {}
    assert count_operations_by_category(operations_for_re_collections, ["wrong_cat"]) == {}


def test_count_operations_by_category_wrong_type(operations_for_re_collections):
    assert count_operations_by_category(operations_for_re_collections, [2222]) == {}
    with pytest.raises(TypeError):
        count_operations_by_category({"description": "Открытие вклада"}, ["Открытие вклада"])
