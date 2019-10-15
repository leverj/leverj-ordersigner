# Leverj Spot Exchange Python Module for Signing Orders

## Description

A python module for signing [leverj](https://leverj.io) spot exchange orders

### Installation
```shell
$ pip install leverj-ordersigner
```

### Usage
```python
from lever_ordersigner import sign_order
sign_order(order, order_instrument, signer)
```


### Development

#### setup
> ensure a python3 virtual env exists in `.venv`, i.e.: `python3 -m venv .venv`
```shell
$ source setup.sh
```

#### test
```shell
$ nosetests
```

#### build
```shell
$ python setup.py sdist
```

