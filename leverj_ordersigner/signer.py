from eth_utils import to_checksum_address
from eth_utils.conversions import to_int
from eth_utils import to_wei
from web3 import Web3
from web3.auto import w3


def sign_order(order, order_instrument, signer):
    (abi_types, evm_parameters) = _get_evm_parameters(
        order, order_instrument, signer)
    keccak_hash = _get_hash(abi_types, evm_parameters)
    signature = sign(keccak_hash, signer)
    return signature


def _get_evm_parameters(order, order_instrument, signer):
    abi_types = []
    evm_parameters = []

    # addresses
    addresses = []
    addresses.append(to_checksum_address(order['accountId']))
    addresses.extend([to_checksum_address(order_instrument['quote']['address']),
                      to_checksum_address(order_instrument['base']['address'])])

    # uints
    p = _convert_to_uint(order['price'], order_instrument['base']['decimals'])
    price_adjusted_for_quote_currency = _adjust_price_for_quote_currency(
        p, order_instrument)
    uints = [to_int(order['timestamp']),
             to_int(_get_order_type_as_int(order['orderType'])),
             to_int(_get_side_as_int(order['side'])),
             _convert_to_uint(order['quantity'], order_instrument['quote']['decimals']), price_adjusted_for_quote_currency]

    bytes32s = []

    # return evm_parameters
    evm_parameters.extend(addresses)
    abi_types.extend(['address']*len(addresses))
    evm_parameters.extend(uints)
    abi_types.extend(['uint256']*len(uints))
    evm_parameters.extend(bytes32s)
    abi_types.extend(['bytes32']*len(bytes32s))
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


def _adjust_price_for_quote_currency(base_price, order_instrument):
    quote_decimals = order_instrument['quote']['decimals']
    print(f"quote_decimals: {quote_decimals}")
    quote_divisor = pow(10, quote_decimals)
    return int(base_price / quote_divisor)


def _convert_to_uint(number, decimals):
    divisor = pow(10, (18 - decimals))
    lowest_denomination_value = to_wei(number, 'ether')
    print(f'lowest_denomination_value: {lowest_denomination_value}')
    return int(lowest_denomination_value / divisor)


def _get_hash(abi_types, evm_parameters):
    # return keccak_hash
    print(f"abi_types: {abi_types}")
    print(f"evm_parameters: {evm_parameters}")
    return Web3.soliditySha3(abi_types, evm_parameters)


def sign(hash, signer):
    print(f"hash: {hash.hex()}")
    signed_message = w3.eth.account.signHash(hash, signer)
    print(f"signed_message: {signed_message}")
    return signed_message.signature.hex()
