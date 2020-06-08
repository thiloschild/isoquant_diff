import setuptools
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="isoquant_diff",
    version="0.0.14",
    author="Thilo Schild",
    author_email="work@thilo-schild.de",
    description="Find the difference between 2 Isoquant configs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiloschild/isoquant_diff",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    packages=setuptools.find_packages(),
    install_requires=['configparser', 'pandas', 'xlrd', 'openpyxl', 'argparse', 'easygui'],
    python_requires='>=3.6',
    entry_points={

        'console_scripts': [
            'isoquant_diff = isoquant_diff.isoquant_diff:main'
        ],
        
    }
)