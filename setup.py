#!/usr/bin/env python
from setuptools import find_packages, setup
import versioneer

README = open('README.rst', 'r').read()


setup(
    name='python-language-server',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Python Language Server for the Language Server Protocol',

    long_description=README,

    # The project's main homepage.
    url='https://github.com/palantir/python-language-server',

    author='Palantir Technologies, Inc.',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'test']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'configparser; python_version<"3.0"',
        'future>=0.14.0',
        'futures; python_version<"3.2"',
        'jedi>=0.13.2',
        'python-jsonrpc-server>=0.1.0',
        'pluggy'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[test]
    extras_require={
        'all': [
            'autopep8',
            'mccabe',
            'pycodestyle',
            'pydocstyle>=2.0.0',
            'pyflakes>=1.6.0',
            'rope>=0.10.5',
            'yapf',
        ],
        'autopep8': ['autopep8'],
        'mccabe': ['mccabe'],
        'pycodestyle': ['pycodestyle'],
        'pydocstyle': ['pydocstyle>=2.0.0'],
        'pyflakes': ['pyflakes>=1.6.0'],
        'rope': ['rope>0.10.5'],
        'yapf': ['yapf'],
        'test': ['versioneer', 'pylint', 'pytest', 'mock', 'pytest-cov', 'coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'upyls = upyls.__main__:main',
        ],
        'upyls': [
            'autopep8 = upyls.plugins.autopep8_format',
            'jedi_completion = upyls.plugins.jedi_completion',
            'jedi_definition = upyls.plugins.definition',
            'jedi_hover = upyls.plugins.hover',
            'jedi_highlight = upyls.plugins.highlight',
            'jedi_references = upyls.plugins.references',
            'jedi_signature_help = upyls.plugins.signature',
            'jedi_symbols = upyls.plugins.symbols',
            'mccabe = upyls.plugins.mccabe_lint',
            'preload = upyls.plugins.preload_imports',
            'pycodestyle = upyls.plugins.pycodestyle_lint',
            'pydocstyle = upyls.plugins.pydocstyle_lint',
            'pyflakes = upyls.plugins.pyflakes_lint',
            'rope_completion = upyls.plugins.rope_completion',
            'rope_rename = upyls.plugins.rope_rename',
            'yapf = upyls.plugins.yapf_format',
        ]
    },
)
