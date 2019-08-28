# Leverj.io Spot Exchange Python Bridge for Signing Orders

## Description

A python bridge to javascript libraries for Leverj.io Spot Exchange

### Installation
> ensure `node` and `yarn` are installed on target machine
```shell
$ pip install leverj_ordersigner
```

### Usage
```python
run_js(command, arguments_as_dictionary)
```

######_commnads_
- compute_signature_for_exchange_order



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

