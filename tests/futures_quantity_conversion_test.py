from nose.tools import *

from leverj_ordersigner import futures

test_data = [
    {'quantity': 1.056, 'numerator': 1056, 'denominator': 1000},
    {'quantity': 0.00567, 'numerator': 567, 'denominator': 100000},
    {'quantity': 1.006, 'numerator': 1006, 'denominator': 1000},
    {'quantity': 0.06, 'numerator': 6, 'denominator': 100},
    {'quantity': 1.000, 'numerator': 1, 'denominator': 1}
]


def test_quanity_conversion_to_numerator_and_denominator():
    for data in test_data:
        (result_numerator, result_denominator) = futures.get_quantity_numerator_and_denominator(
            data['quantity'])
        print(
            f'result_numerator: {result_numerator}, result_denominator: {result_denominator}')
        assert_equal(result_numerator, data['numerator'])
        assert_equal(result_denominator, data['denominator'])
