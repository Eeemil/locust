# -*- coding: utf-8 -*-
import ast
import os
import re

from setuptools import find_packages, setup


# parse version from locust/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
_init_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locust", "__init__.py")
with open(_init_file, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Dependencies are defined in requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='locustio',
    version=version,
    description="Website load testing framework",
    long_description="""Locust is a python utility for doing easy, distributed load testing of a web site""",
    classifiers=[
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    keywords='',
    author='Jonatan Heyman, Carl Bystrom, Joakim Hamrén, Hugo Heyman',
    author_email='',
    url='https://locust.io/',
    license='MIT',
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    test_suite="locust.test",
    tests_require=['mock'],
    entry_points={
        'console_scripts': [
            'locust = locust.main:main',
        ]
    },
)
