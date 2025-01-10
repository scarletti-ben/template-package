
# < ==================================================================
# < Imports
# < ==================================================================

from setuptools import setup, find_packages

# < ==================================================================
# < Settings
# < ==================================================================

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

# < ==================================================================
# < Execution
# < ==================================================================

setup(
    author = AUTHOR,
    name = PACKAGE_NAME,
    version = VERSION,
    url = URL,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = LONG_DESCRIPTION_TYPE,
    package_dir = {'': PACKAGE_LOCATION},
    packages = find_packages(where = PACKAGE_LOCATION),
    author_email = EMAIL,
    license = LICENSE,
    description = DESCRIPTION,
    python_requires = PYTHON_VERSION,
    install_requires = REQUIREMENTS,
)