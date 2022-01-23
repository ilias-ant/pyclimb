# pyclimb

[![PyPI](https://img.shields.io/pypi/v/pyclimb?color=blue&label=PyPI&logo=PyPI&logoColor=white)](https://pypi.org/project/pyclimb/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyclimb?logo=python&logoColor=white)](https://www.python.org/) [![codecov](https://codecov.io/gh/ilias-ant/pyclimb/branch/main/graph/badge.svg?token=2H0VB8I8IH)](https://codecov.io/gh/ilias-ant/pyclimb) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ilias-ant/pyclimb/CI)](https://github.com/ilias-ant/pyclimb/actions/workflows/ci.yml) 
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyclimb?color=orange)](https://www.python.org/dev/peps/pep-0427/)

A library to easily convert climbing route grades between different grading systems.

In rock climbing, mountaineering, and other climbing disciplines, climbers give a grade to a climbing route or boulder problem, intended to describe concisely the difficulty and danger of climbing it. Different types of climbing (such as sport climbing, bouldering or ice climbing) each have their own grading systems, and many nationalities developed their own, distinctive grading systems.

## Install

The recommended installation is via `pip`:

```bash
pip install pyclimb
```

## Usage

```python
import pyclimb


pyclimb.convert(grade='6a+', to='YDS')
// '5.10b'
pyclimb.convert(grade='9c', to='YDS')
// '5.15d'
```

## Note

This is a package under active development. Currently, only the following conversions are being supported:

- [sport climbing] conversion from the French grading system to the YDS ([Yosemite Decimal System](https://en.wikipedia.org/wiki/Yosemite_Decimal_System)).

Other conversions and different types of climbing will be included soon. These changes may drastically change the user-facing API, so do consult the semantic versioning of this package before upgrading to a newer version.

## How to contribute

If you wish to contribute, [this](CONTRIBUTING.md) is a great place to start!

## License

Distributed under the [MIT License](LICENSE).
