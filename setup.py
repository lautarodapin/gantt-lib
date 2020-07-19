import setuptools
from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='python-gantt-lautarodapin',
    version='0.0.1',
    description='Extension of `python-gantt` with added functionality for django',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=[
        "python-gantt~=0.6.0"
    ],
    classifiers=[
        "Programming Language :: Python ::3",
        "Programming Language :: Python ::3.7",
        "Programming Language :: Python ::3.8",
        "License :: MIT License"
    ]
)