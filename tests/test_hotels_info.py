import validators
from hotels import info


def test_hotel_name():
    for key in info.keys():
        assert isinstance(key, str)


def test_hotel_url():
    for value in info.values():
        h_url = value[0]
        assert validators.url(h_url)


def test_hotel_filter():
    for value in info.values():
        h_filter = value[1]
        assert isinstance(h_filter, str)


def test_hotel_sheet():
    for value in info.values():
        h_sheet = value[2]
        assert isinstance(h_sheet, int)


def test_hotel_sheet_increment():
    temp = 2
    for value in info.values():
        h_sheet = value[2]
        assert h_sheet == temp
        temp += 4
