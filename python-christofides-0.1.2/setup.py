try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-christofides',
    version='0.1.2',
    author='D. S. Rahul',
    author_email='dsrahul@outlook.com',
    packages=['pyChristofides', 'pyChristofides.test'],
    url='http://pypi.python.org/pypi/python-christofides/',
    license='LICENSE.txt',
    description='Implementation of Christofides Algorithm for TSP in python.',
    long_description=open('README.txt').read(),
    install_requires=[
        "scipy >= 0.13.3",
        "networkx >= 1.11rc1",
		"numpy >= 1.8.2",
		"munkres >= 1.0.7"	
    ],
)
