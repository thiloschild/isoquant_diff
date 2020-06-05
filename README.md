# Isoquant_diff

Isoquant_diff is a Python library that works with the  Isoquant Software. It can find the differences between two config files.
It supports .ini and .xlsx files.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install isoquant_diff.

```bash
pip install isoquant_diff
```

## Usage

Once the package is installed you can call ist from the command line or in a python script.

This package will ask for two file in the command prompt and will create an excel file and html file with all differences.

Cmd:

```bash
isoquant_diff
```

Python:
```python
import isoquant_diff

isoquant_diff.main() 
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
