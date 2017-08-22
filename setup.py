from setuptools import setup, find_packages

setup(
    name='py_public_polo',
    description='Poloniex Public API client',
    long_description='Poloniex Public API client',
    version='0.5',
    url='https://github.com/dattnguyen82/py_public_polo',
    author='Dat Nguyen',
    keywords='poloniex',
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=['requests'],
    zip_safe=False
)