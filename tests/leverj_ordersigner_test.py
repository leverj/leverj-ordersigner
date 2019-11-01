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
    'signature': '0xaad62800f307299a33dae10908c559bd7cd4658a3803e6b587e0f5bf95a052c17783324ec07b629c30e3a41eb20b4ace2787304c50a00b5cdcbd6bc22dbbded11b'
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
    'signature': '0xc393a676add35be168f5df829f742e9685020abfcdc94a4caae47488b92f5e886a96a33e9d56239613c3649d7c0c53d376c28fb3f82a873c5766e2607e1c4f501c'
}


def test_sign_order():
    result = sign_order(buy['order'], instrument, buy['signer'])
    assert_equal(result, buy['signature'])
    assert_not_equal(result, sell['signature'])

    result = sign_order(sell['order'], instrument, sell['signer'])
    assert_equal(result, sell['signature'])
    assert_not_equal(result, buy['signature'])
