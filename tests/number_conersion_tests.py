from nose.tools import *
from leverj_ordersigner import *

data = [
    {"number": 10135.1941, "decimals": 18, "result": 10135194100000000000000},
    {"number": 10135.1941, "decimals": 8, "result": 1013519410000},
]


def test_number_conversion():
    for each in data:
        result = convert_to_unit_lowest_denomination(each["number"], each["decimals"])
        assert_equal(result, each["result"])
