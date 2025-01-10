# Template Package
The purpose of this package is to serve as a template for my future python packages.

The different branches of this repository will each have a slightly different way of structuring a python package. The first structure I learned was `setup.py` which seems to be the older method of doing things, and is missing some of the quality-of-life features that you can find with structures including `setup.cfg`, `pyproject.toml`, or a dependency manager like [`Poetry`](https://python-poetry.org/).

### Branch Information
This branch relies primarily on a `pyproject.toml` file and is a newer approach of package structuring
- The other branch which relies on a `setup.py` file can be found [here](https://github.com/scarletti-ben/template-package/tree/with-setup-py)

# Installing a Local Package via `pip`
If you have a local package on your system that hasn't been installed via pip, navigate to the package's root directory and run `pip install .`, this will install the package to python's `site-packages` folder, much like a regular package hosted on `PyPi`.

Sometimes, when you are developing a package, you want to be able to edit it without having to uninstall or reinstall it. One way to do this is to install the local package in editable mode via `pip install -e .`.This will create a symbolic link to the local package in python's `site-packages` folder, and will create a `template-package.egg-link` for your package. If you change the files in your package, changes will be reflected immediately in the installed version.

# Installing from GitHub via `pip`
You can install a package from `GitHub` using one of the methods listed below

- Clone the repository and install to `site-packages`
  - `git clone https://github.com/scarletti-ben/template-package`
  - `pip install ./template-package`

- Clone the repository and install in editable mode, for development
  - `git clone https://github.com/scarletti-ben/template-package`
  - `pip install -e ./template-package`

- Installing from the default branch to `site-packages`
  - `pip install git+https://github.com/scarletti-ben/template-package.git`

- Installing from a specficic branch e.g. `main` to `site-packages`
  - `pip install git+https://github.com/scarletti-ben/template-package.git@main`

- Installing from archive link to `site-packages`
  - `pip install https://github.com/scarletti-ben/template-package/archive/master.zip`

- Install in editable mode for development
  - `pip install -e git+https://github.com/scarletti-ben/template-package.git`

# Miscellaneous

### Notes About `pip`
Python's package installer is called `pip` and it allows you to install packages that are hosted on the package index [`PyPi`](https://pypi.org/), hosted on [`GitHub`](https://github.com/) or even locally from your system.

By default, if you are not working in a virtual environment, `pip` installs packages to the `site-packages` folder.

### Notes About Building and Distribution
A distribution package includes metadata and resources for installation, while an import package contains the actual code. When deciding on a project structure you can mix and match `setup.py`, `setup.cfg` and `pyproject.toml`, their main aim is to instruct pip how to build your package or how to install it, and apply the correct metadata. Modern packages typically rely on `pyproject.toml` for building / installing and metadata, and may include `setup.py` for compatability. A pure `setup.py` approach still uses `setuptools` for building / installing implicitly, whereas a `pyproject.toml` might use another backend or specify `setuptools` as below
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```
- Files from the install process, when running `pip install .`, such as `.whl` (`wheel`) files, wil be placed in a folder called `build`
- Files from the build process, when running `python -m build` will be placed in a folder called `dist`
- `.whl` and `.tar.gz` files from `python -m build` in the `dist` folder are the files that are uploaded for distribution on `PyPi`

### Example Command Line Output When Installing a Package
- Installing a local package in editable mode
```

- Checking that the package is installed
```
```

- Uninstalling the package
```
```
