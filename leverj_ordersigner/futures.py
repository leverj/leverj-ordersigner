from eth_utils import to_checksum_address
from eth_utils.conversions import to_int
from eth_utils import to_wei
from web3 import Web3
from web3.auto import w3
from decimal import *


def sign_order(order, order_instrument, signer):
    (abi_types, evm_parameters) = _get_evm_parameters(
        order, order_instrument, signer)
    # solidity pack into bytes
    keccak_hash = _get_hash(abi_types, evm_parameters)
    signature = sign(keccak_hash, signer)
    return signature


def _get_evm_parameters(order, order_instrument, signer):
    abi_types = []
    evm_parameters = []

    # account
    abi_types.append('address')
    evm_parameters.append(to_checksum_address(order['accountId']))

    # originatorTimestamp
    abi_types.append('uint64')
    evm_parameters.append(to_int(order['timestamp']))

    # orderType
    abi_types.append('uint8')
    evm_parameters.append(to_int(_get_order_type_as_int(order['orderType'])))

    # side
    abi_types.append('uint8')
    evm_parameters.append(to_int(_get_side_as_int(order['side'])))

    # instrument
    abi_types.append('uint32')
    evm_parameters.append(int(order['instrument']))

    # price
    abi_types.append('uint256')
    price = _convert_to_unit_lowest_denomination(
        order['price'], order_instrument['quote']['decimals'])
    evm_parameters.append(price)

    # marginPerUnit
    abi_types.append('uint256')
    evm_parameters.append(to_int(int(order['marginPerFraction'])))

    # asset
    abi_types.append('address')
    evm_parameters.append(to_checksum_address(order['quote']))

    # quantity
    (numerator, denominator) = get_quantity_numerator_and_denominator(
        order['quantity'])
    abi_types.append('uint64')
    evm_parameters.append(to_int(numerator))
    abi_types.append('uint64')
    evm_parameters.append(to_int(denominator))

    return (abi_types, evm_parameters)


def _get_order_type_as_int(order_type):
    order_dict = {
        'LMT': 1,
        'MKT': 2,
        'SLM': 3,
        'STM': 4
    }
    return order_dict[order_type]


def _get_side_as_int(side):
    side_dict = {
        'buy': 1,
        'sell': 2
    }
    return side_dict[side]


def convert_to_unit_lowest_denomination(number, decimals):
    return _convert_to_unit_lowest_denomination(number, decimals)


def _convert_to_unit_lowest_denomination(number, decimals):
    number_in_wei = w3.toWei(number, 'ether')
    str_number = str(number_in_wei)
    final_value = str_number[:(len(str_number) - (18-decimals))]
    return int(final_value)


def get_quantity_numerator_and_denominator(quantity):
    decimal_places = _numbers_after_decimal_point(quantity)
    str_quantity = str(quantity)
    numerator = _strip_unnecessary_zeros(str_quantity).replace('.', '')
    denominator = pow(10, decimal_places)
    print(
        f'quantity: {quantity}, decimal_places: {decimal_places}, numerator: {int(numerator)}, denominator: {int(denominator)}')
    return (int(numerator), int(denominator))


def _strip_unnecessary_zeros(number_as_string):
    return number_as_string.rstrip('0').rstrip('.') if '.' in number_as_string else number_as_string


def _numbers_after_decimal_point(x):
    s = str(x)
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1


def _get_hash(abi_types, evm_parameters):
    # return keccak_hash
    return Web3.soliditySha3(abi_types, evm_parameters)


def sign(hash, signer):
    signed_message = w3.eth.account.signHash(hash, signer)
    return signed_message.signature.hex()
