'''
Created on Nov 11, 2012

@author: ashwin
'''

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

requires = ['tqdm', 'colorama', 'pystitia']

setup(
	name = 'Pyvolution',
	version = "2.0",
	description = "Evolutionary Algorithms Framework",
	long_description="Evolutionary Algorithms Framework",
	author = 'Ashwin Panchapakesan',
	author_email = 'ashwin.panchapakesan@gmail.com',
	url = 'https://github.com/inspectorG4dget/Genetic-Framework',
	packages = ["pyvolution"],
	include_package_data = True,
	install_requires = requires,
	license = "Apache License, Version 2.0",
	zip_safe = False,
	classifiers = (
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.7',
	),
)