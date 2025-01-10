# Template Package
The purpose of this package is to serve as a template for my future python packages.

The different branches of this repository will each have a slightly different way of structuring a python package. The first structure I learned was `setup.py` which seems to be the older method of doing things, and is missing some of the quality-of-life features that you can find with structures including `setup.cfg`, `pyproject.toml`, or a dependency manager like [`Poetry`](https://python-poetry.org/).

### Branch Information
This branch relies on `setup.py` and is an older approach of package structuring
- The other branch which uses a `pyproject.toml` file can be found [here](https://github.com/scarletti-ben/template-package/tree/with-pyproject-toml)

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
- Installing a local package in regular mode
```cmd
C:\...\template-package> pip install .
Processing C:\...\template-package
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: template-package
  Building wheel for template-package (setup.py) ... done
  Created wheel for template-package: filename=template_package-0.1.0-py3-none-any.whl size=4249 sha256=...
  Stored in directory: C:\...\...
Successfully built template-package
Installing collected packages: template-package
Successfully installed template-package-0.1.0
```

- Installing a local package in editable mode
```cmd
C:\...\template-package> pip install -e .
Obtaining file:///C:/.../template-package
  Preparing metadata (setup.py) ... done
Installing collected packages: template-package
  Running setup.py develop for template-package
Successfully installed template-package-0.1.0
```

- Checking that the package is installed
```cmd
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
```

- Uninstalling the package
```cmd
C:\...\template-package> pip uninstall template-package
Found existing installation: template-package 0.1.0
Uninstalling template-package-0.1.0:
  Would remove:
    C:\...\python\site-packages\template-package.egg-link
Proceed (Y/n)? y
  Successfully uninstalled template-package-0.1.0
```

- Building the package for `PyPi`
```powershell
PS A\template-package> python -m build .
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools >= 40.8.0
* Getting build dependencies for sdist...
running egg_info
writing src\template_package.egg-info\PKG-INFO
writing dependency_links to src\template_package.egg-info\dependency_links.txt
writing top-level names to src\template_package.egg-info\top_level.txt        
reading manifest file 'src\template_package.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src\template_package.egg-info\SOURCES.txt'
* Building sdist...
running sdist
running egg_info
writing src\template_package.egg-info\PKG-INFO
writing dependency_links to src\template_package.egg-info\dependency_links.txt
writing top-level names to src\template_package.egg-info\top_level.txt
reading manifest file 'src\template_package.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src\template_package.egg-info\SOURCES.txt'
running check
creating template_package-0.1.0
creating template_package-0.1.0\src\template_package
creating template_package-0.1.0\src\template_package.egg-info
copying files to template_package-0.1.0...
copying LICENSE -> template_package-0.1.0
copying README.md -> template_package-0.1.0
copying setup.py -> template_package-0.1.0
copying src\template_package\__init__.py -> template_package-0.1.0\src\template_package
copying src\template_package\moduleA.py -> template_package-0.1.0\src\template_package
copying src\template_package.egg-info\PKG-INFO -> template_package-0.1.0\src\template_package.egg-info
copying src\template_package.egg-info\SOURCES.txt -> template_package-0.1.0\src\template_package.egg-info
copying src\template_package.egg-info\dependency_links.txt -> template_package-0.1.0\src\template_package.egg-info
copying src\template_package.egg-info\top_level.txt -> template_package-0.1.0\src\template_package.egg-infocopying src\template_package.egg-info\SOURCES.txt -> template_package-0.1.0\src\template_package.egg-info
Writing template_package-0.1.0\setup.cfg
Creating tar archive
removing 'template_package-0.1.0' (and everything under it)
* Building wheel from sdist
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools >= 40.8.0
* Getting build dependencies for wheel...
running egg_info
writing src\template_package.egg-info\PKG-INFO
writing dependency_links to src\template_package.egg-info\dependency_links.txt
writing top-level names to src\template_package.egg-info\top_level.txt
reading manifest file 'src\template_package.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src\template_package.egg-info\SOURCES.txt'
* Building wheel...
running bdist_wheel
running build
running build_py
creating build\lib\template_package
copying src\template_package\moduleA.py -> build\lib\template_package
copying src\template_package\__init__.py -> build\lib\template_package
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\template_package
copying build\lib\template_package\moduleA.py -> build\bdist.win-amd64\wheel\.\template_package
copying build\lib\template_package\__init__.py -> build\bdist.win-amd64\wheel\.\template_package
running install_egg_info
running egg_info
writing src\template_package.egg-info\PKG-INFO
writing dependency_links to src\template_package.egg-info\dependency_links.txt
writing top-level names to src\template_package.egg-info\top_level.txt
reading manifest file 'src\template_package.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src\template_package.egg-info\SOURCES.txt'
Copying src\template_package.egg-info to build\bdist.win-amd64\wheel\.\template_package-0.1.0-py3.10.egg-info
running install_scripts
creating build\bdist.win-amd64\wheel\template_package-0.1.0.dist-info\WHEEL
creating 'C:\...\template-package\dist\.tmp-hys3oqg9\template_package-0.1.0-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'template_package/__init__.py'
adding 'template_package/moduleA.py'
adding 'template_package-0.1.0.dist-info/LICENSE'
adding 'template_package-0.1.0.dist-info/METADATA'
adding 'template_package-0.1.0.dist-info/WHEEL'
adding 'template_package-0.1.0.dist-info/top_level.txt'
adding 'template_package-0.1.0.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
Successfully built template_package-0.1.0.tar.gz and template_package-0.1.0-py3-none-any.whl
```