from eth_utils import to_checksum_address
from eth_utils.conversions import to_int
from eth_utils import to_wei
from web3 import Web3
from web3.auto import w3


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

    # quantity
    abi_types.append('uint256')
    quantity = _convert_to_unit_lowest_denomination(
        order['quantity'], order_instrument['base']['decimals'])
    evm_parameters.append(quantity)

    # price
    abi_types.append('uint256')
    price = _convert_to_unit_lowest_denomination(
        order['price'], order_instrument['quote']['decimals'])
    evm_parameters.append(price)

    # base
    abi_types.append('address')
    evm_parameters.append(to_checksum_address(
        order_instrument['base']['address']))

    # quote
    abi_types.append('address')
    evm_parameters.append(to_checksum_address(
        order_instrument['quote']['address']))

    return (abi_types, evm_parameters)


def _get_order_type_as_int(order_type):
    order_dict = {
        'LMT': 1,
        'MKT': 2
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


def _get_hash(abi_types, evm_parameters):
    # return keccak_hash
    return Web3.soliditySha3(abi_types, evm_parameters)


def sign(hash, signer):
    signed_message = w3.eth.account.signHash(hash, signer)
    return signed_message.signature.hex()
