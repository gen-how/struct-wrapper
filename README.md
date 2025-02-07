# struct-wrapper

This package provides wrapper classes for Python standard library [`struct`](https://docs.python.org/3/library/struct.html) to simplify [format strings](https://docs.python.org/3/library/struct.html#format-strings).

## Installation

```
pip install git+https://github.com/gen-how/struct-wrapper.git
```

## Examples

```python
>>> from struct_wrapper import U16
>>> U16.size
2
>>> U16.frombytes(b"\x20\x00")
32
>>> U16.tobytes(1024)
b'\x00\x04'
```
