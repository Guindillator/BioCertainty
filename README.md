# Python Package for certainty in bio-scholarly statements

## How to install the package
Install via `pip`:

```
pip install git+https://github.com/Guindillator/BioCertainty.git
```

 - TODO: add to [PyPI](https://pypi.org/)

## Usage example
```python
Import biocertainty as B

a = PMCID or DOI
b = statement

certainty = B.Certainty(b)

#Either PMCID or DOI
nanopublication = B.Nanopublication(a, b)

# 'a' MUST be DOI
micropublication = B.Micropublication (a, b)

## Documentation
* Documentation can be found in the `docs` folder.

## Software citation
Mario Prieto Godoy & Mark Wilkinson. (2019, July 18). Guindillator/BioCertainty: First bio-certainty identifier (Version v0.1.0).

# License
Copyright (c) 2018, Wilkinson Laboratory for Biological Informatics

MIT license
