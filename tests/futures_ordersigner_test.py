from nose.tools import *

from leverj_ordersigner import futures

BTCDAI_instrument = {
    'id': '1',
    'symbol': 'BTCDAI',
    'name': 'BTC/DAI',
    'status': 'active',
    'tickSize': 1,
    'quoteSignificantDigits': 0,
    'baseSignificantDigits': 4,
    'baseSymbol': 'BTC',
    'quoteSymbol': 'DAI',
    'maxLeverage': 100,
    'topic': 'index_BTCUSD',
    'quote': {
        'name': 'DAI',
        'address': '0xb0F776EB352738CF25710d92Fca2f4A5e2c24D3e',
        'symbol': 'DAI',
        'decimals': 18
    }
}

buy = {
    'order': {
        'accountId': '0xc21b183A8050D1988117B86408655ff974d021A0',
        'originator': '0x10758C328A02B511d2a7B8f55459929Fa760411f',
        'instrument': BTCDAI_instrument['id'],
        'price': round(float(9380), BTCDAI_instrument['quoteSignificantDigits']),
        'quantity': round(float(1), BTCDAI_instrument['baseSignificantDigits']),
        'marginPerFraction': '191428571428571430000',
        'side': 'buy',
        'orderType': 'SLM',
        'timestamp': 1595560081494041,
        'quote': BTCDAI_instrument['quote']['address'],
        'isPostOnly': False,
        'reduceOnly': False,
        'clientOrderId': 1,
        'triggerPrice': 9385
    },
    'signer': '0xae9edfad7fa29b0d6e14b045b5e74f3360e041545cf64236e81e616849072d65',
    'signature': '0xe367a6d7ec746c8e987758bc9109fcd4c8f73880a4706b024d72aa2eb5abf2e571754db5fa65ce418781474a9c5319482d124a78c5bbe822d60e6383fac80e231c'
}

sell = {
    'order': {
        'accountId': '0xc21b183A8050D1988117B86408655ff974d021A0',
        'originator': '0x10758C328A02B511d2a7B8f55459929Fa760411f',
        'instrument': BTCDAI_instrument['id'],
        'price': round(float(9380), BTCDAI_instrument['quoteSignificantDigits']),
        'quantity': round(float(1), BTCDAI_instrument['baseSignificantDigits']),
        'marginPerFraction': '191428571428571430000',
        'side': 'sell',
        'orderType': 'SLM',
        'timestamp': 1595560081494041,
        'quote': BTCDAI_instrument['quote']['address'],
        'isPostOnly': False,
        'reduceOnly': False,
        'clientOrderId': 1,
        'triggerPrice': 9385
    },
    'signer': '0xae9edfad7fa29b0d6e14b045b5e74f3360e041545cf64236e81e616849072d65',
    'signature': '0x057c47d70ac6220e25f95063d701411e011fde46a3a3065e9a3b3f6f4388dc570e16c058860733f7b2baabc23e460931b588cc3b0f3be94b4b3b497b8ada15581c'
}


def test_sign_order():
    result = futures.sign_order(buy['order'], BTCDAI_instrument, buy['signer'])
    assert_equal(result, buy['signature'])
    assert_not_equal(result, sell['signature'])

    result = futures.sign_order(
        sell['order'], BTCDAI_instrument, sell['signer'])
    assert_equal(result, sell['signature'])
    assert_not_equal(result, buy['signature'])
