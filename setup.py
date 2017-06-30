"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# copy contents of readme.md to readme for python package 
if not path.exists("README.rst"):
	readme = open("README.rst", 'w')
	readme.write(long_description)
	readme.close()

setup(
    name='farbsort',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
	# using the reverse date as version number to avoid  discussion what makes a version 1.0
	# yyyy.(m)m.(d)d if you have more than one version a day append hour and minutes
    version='2017.6.30',

    description='the websocket server for the AMP showcase',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/bbvch/farbsort-websocket',

    # Author details
    author='Embedded Community @bbv',
    author_email='info@bbv.ch',

    # Choose your license
#    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
 #       'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
#        'Intended Audience :: Developers',
#        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
#        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        
    ],

    # What does your project relate to?
    keywords='farbsort-gui pru-farbsort',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['tornado'],

	python_requires='>=2.7, <3',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        '': ['farbsort.html', 'README.md'],
    },


    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'server=server:main',
        ],
    },
)

