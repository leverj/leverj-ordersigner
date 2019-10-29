from nose.tools import *
from leverj_ordersigner import *

instrument = {
    'symbol': 'LEVETH',
    'quote': {
        'address': '0x0000000000000000000000000000000000000000',
        'decimals': 18
    },
    'base': {
        'address': '0x167cdb1aC9979A6a694B368ED3D2bF9259Fa8282',
        'decimals': 9
    }
}

buy = {
    'order': {
        'accountId': '0x167cdb1aC9979A6a694B368ED3D2bF9259Fa8282',
        'side': 'buy',
        'quantity': 12.3343,
        'price': 23.44322,
        'orderType': 'LMT',
        'instrument': 'LEVETH',
        'timestamp': 12382173200872,
        'expiryTime': 1238217320021122,
    },
    'signer': '0xb98ea45b6515cbd6a5c39108612b2cd5ae184d5eb0d72b21389a1fe6db01fe0d',
    'signature': '0x94d197d0ea127fc263ce7aefc25f2edc4911de80c5614d9bbd5654613032dabb0420aafadd6251727943b8460b8f543455b40bbdc29ffb1f7cf59fc8273d206b1c'
}

sell = {
    'order': {
        'accountId': '0x167cdb1aC9979A6a694B368ED3D2bF9259Fa8282',
        'side': 'sell',
        'quantity': 12.3343,
        'price': 23.44322,
        'orderType': 'LMT',
        'instrument': 'LEVETH',
        'timestamp': 12382173200872,
        'expiryTime': 1238217320021122
    },
    'signer': '0xb98ea45b6515cbd6a5c39108612b2cd5ae184d5eb0d72b21389a1fe6db01fe0d',
    'signature': '0xaddab6976e5f01fd63db57376da178ee6f7a972ca3480a545f668fea7291be2c2e13b2c6a54d0f00179fcee3503eb2615f545986534cb2f1891f0ce4243e6f251c'
}


def test_sign_order():
    result = sign_order(buy['order'], instrument, buy['signer'])
    assert_equal(result, buy['signature'])
    assert_not_equal(result, sell['signature'])

    result = sign_order(sell['order'], instrument, sell['signer'])
    assert_equal(result, sell['signature'])
    assert_not_equal(result, buy['signature'])
