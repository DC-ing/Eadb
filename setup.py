#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/16 17:37
# Author  : gaojiewen
# Version : 1.0
# Desc    :

import os
import io
import sys

from shutil import rmtree
from setuptools import find_packages, setup, Command

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'eadb', '__about__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

install_requires = []


class UploadCommand(Command):
    """Support setup.py upload. copy from
    https://github.com/kenneth-reitz/setup.py/blob/master/setup.py"""

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires='>=3.0, <4',
    packages=find_packages(exclude=["examples", "tests", "tests.*"]),
    install_requires=install_requires,
    keywords='Android adb',
    extras_require={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'eadb=eadb.cli:main_eadb',
            'adscreen=eadb.cli:get_screenshot',
            'adversion=eadb.cli:get_version',
            'adname=eadb.cli:get_name',
            'adinfo=eadb.cli:get_info',
        ]
    },
    cmdclass={
        'upload': UploadCommand
    }
)
