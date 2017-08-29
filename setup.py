# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='mundipagg_one_python',
    version='1.0.1',
    url='https://github.com/meuspedidos/mundipagg_one_python',
    license='Apache',
    author='MundiPagg',
    author_email='developers@mundipagg.com',
    description='Sdk for integration with mundipagg payment api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Apache 2 License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Gateway Integration :: SDK',
    ],
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'enum34>=1.0.0',
        'xmltodict>=0.9.2'
    ],
    keywords=[
        'mundipagg',
        'rest',
        'sdk',
        'payments',
    ]
)
