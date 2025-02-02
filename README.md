# Noom


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Usage

### Installation

Install latest from the GitHub
[repository](https://github.com/vinay-jose/noom):

``` sh
$ pip install git+https://github.com/vinay-jose/noom.git
```

or from [pypi](https://pypi.org/project/noom/)

``` sh
$ pip install noom
```

### Documentation

Documentation can be found hosted on this GitHub
[repository](https://github.com/vinay-jose/noom)’s
[pages](https://vinayjose.com/noom/). Additionally you can find package
manager specific guidelines on
[conda](https://anaconda.org/vinay-jose/noom) and
[pypi](https://pypi.org/project/noom/) respectively.

## How to use

``` python
a = Noom(2)
b = Noom(7)
```

``` python
a + b
```

    9

``` python
a - b
```

    -5

``` python
a * b
```

    14

``` python
a // b
```

    0

``` python
a / b
```

    0.2857142857142857

``` python
a == b
```

    False

``` python
a < b
```

    True

``` python
a >= b
```

    False

## Developer Guide

If you are new to using `nbdev` here are some useful pointers to get you
started.

### Install noom in Development mode

``` sh
# make sure noom package is installed in development mode
$ pip install -e .

# make changes under nbs/ directory
# ...

# compile to have changes apply to noom
$ nbdev_prepare
```
