# Isoquant_diff

Isoquant_diff is a Python library that works with the  Isoquant Software. It can find the differences between two config files.
It supports .ini and .xlsx files.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install isoquant_diff.

```bash
pip install isoquant_diff
```

## Usage

Once the package is installed you can call isoquant_diff from the command line.

It will ask for two file in the command prompt and will create an excel file and html file with all differences.

Command prompt:

```bash
isoquant_diff [-h] [-c] [-r]
```
-h, --help           show this help message and exit

-c, --csv            output as csv (default: html-file)

-r, --report_unique  compares only parameters which are defined in both config-files


## License
[MIT](https://choosealicense.com/licenses/mit/)