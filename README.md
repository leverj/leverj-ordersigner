# Leverj Spot & Derivatives Exchange Python Module for Signing Orders

## Description

A python module for signing [leverj](https://leverj.io) spot and derivatives exchange orders

### Installation
```shell
$ pip install leverj-ordersigner
```

### Usage

Sign a spot exchange order as follows:

```python
from leverj_ordersigner import spot
spot.sign_order(order, order_instrument, signer)
```

Sign a futures exchange order like so:

```python
from leverj_ordersigner import futures
futures.sign_order(order, order_instrument, signer)
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

