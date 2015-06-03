"""setup.py - install script for pandoc-fignos."""

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

LONG_DESCRIPTION = """\
pandoc-fignos is a pandoc filter for numbering figures and figure references.
"""

setup(
    name='pandoc-fignos',
    version='0.2.1',

    author='Thomas J. Duck',
    author_email='tomduck@tomduck.ca',
    description='Figure number filter for pandoc',
    long_description=LONG_DESCRIPTION,
    license='GPL',
    keywords='pandoc figure numbers filter',
    url='https://github.com/tomduck/pandoc-fignos',
    download_url = 'https://github.com/tomduck/pandoc-fignos/tarball/0.2.1',
    
    install_requires=['pandocfilters', 'pandoc-attributes'],

    py_modules=['pandoc_fignos'],
    entry_points={'console_scripts':['pandoc-fignos = pandoc_fignos:main']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
        ],
)
