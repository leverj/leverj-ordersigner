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

BTCDAI_instrument_2 = {
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
        'address': '0x4F96Fe3b7A6Cf9725f59d353F723c1bDb64CA6Aa',
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

buy_2 = {
    'order': {
        'accountId': '0xc21b183A8050D1988117B86408655ff974d021A0',
        'originator': '0x1d22dd57Ba368784Cd2c6Baf5626d6590EFf5116',
        'instrument': BTCDAI_instrument_2['id'],
        'price': round(float(11317), BTCDAI_instrument_2['quoteSignificantDigits']),
        'quantity': round(float(0.1309), BTCDAI_instrument_2['baseSignificantDigits']),
        'marginPerFraction': '11316900000000000000000',
        'side': 'buy',
        'orderType': 'LMT',
        'timestamp': 1596734143144171,
        'quote': BTCDAI_instrument_2['quote']['address'],
        'isPostOnly': False,
        'reduceOnly': False,
        'clientOrderId': 1,
        'triggerPrice': 11317
    },
    'signer': '0x35c06db4994745c3386ebaac69c6105b0a298eee2ddd09a5ae11ab0fd36dfb41',
    'signature': '0x993fb08bcb495cfebdaee5869fae03f06e2d7d2ac8d0c2ab0d11e148662b188835ba0eb3932c7112953752ada067a0194e8a466740214ad5e2f0402e954ae2df1c'
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

    result = futures.sign_order(
        buy_2['order'], BTCDAI_instrument_2, buy_2['signer'])
    assert_equal(result, buy_2['signature'])
    assert_not_equal(result, buy['signature'])
