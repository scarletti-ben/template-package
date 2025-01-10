# Template Package

The purpose of this package is to serve as a template for future python packages. 

Usage of `setup.py` seems to be the older method of doing things, and is missing some of the quality-of-life features that you can find using `setup.cfg`, `pyproject.toml` or a dependency manager like [`Poetry`](https://python-poetry.org/).

As I am still learning the process of making python packages, the aim is to have different branches of this repository for the different methods of structuring, uploading and installing a python package, hopefully including the methods above eg. `pyproject.toml`.

# Command Line Output
Below is the sort of command line output that is to be expected when installing / checking / uninstalling a package with `setup.py`
```cmd
C:\...\template-package> pip install -e .
Obtaining file:///C:/.../template-package
  Preparing metadata (setup.py) ... done
Installing collected packages: template-package
  Running setup.py develop for template-package
Successfully installed template-package-0.1.0

C:\...\template-package> pip show template-package
Name: template-package
Version: 0.1.0
Summary: Template package for Python
Home-page: https://github.com/username/template-package
Author: username
Author-email: username@email.com
License: MIT
Location: C:\...\template-package\src
Editable project location: C:\...\template-package\src
Requires: 
Required-by:

C:\...\template-package> pip uninstall template-package
Found existing installation: template-package 0.1.0
Uninstalling template-package-0.1.0:
  Would remove:
    C:\...\python\site-packages\template-package.egg-link
Proceed (Y/n)? y
  Successfully uninstalled template-package-0.1.0
```

# The `setup.py` File

```python
AUTHOR = 'username'
EMAIL = 'username@email.com'
PACKAGE_NAME = 'template-package'
VERSION = '0.1.0'
PACKAGE_LOCATION = 'src'
URL = f'https://github.com/{AUTHOR}/{PACKAGE_NAME}'
LICENSE = 'MIT'
DESCRIPTION = 'Template package for Python'
PYTHON_VERSION = '>=3.7'
REQUIREMENTS = []

with open('README.md', "r") as f:
    LONG_DESCRIPTION = f.read()
LONG_DESCRIPTION_TYPE = "text/markdown"
```

# Egg
- Creates `template-package/src/template_package.egg-info` folder
  - Deleted when you uninstall


# Other
In command line `python -c "from template_package.moduleA import test; test()"`