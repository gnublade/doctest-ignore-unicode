import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

setup(
    name="doctest-ignore-unicode",
    version="0.1.0",
    author="Andy Kilner",
    author_email="gnublde@gmail.com",
    description="Add flag to ignore unicode literal prefixes in doctests",
    long_description=read('README.rst'),
    license='Apache License, Version 2.0',
    url="http://github.com/gnublade/doctest-ignore-unicode",
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Apache Software License',
        "Topic :: Software Development :: Testing",
    ],
    py_modules=['nose_plugin'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'doctest_ignore_unicode = nose_plugin:DoctestIgnoreUnicode'
        ]
    },
    install_requires=['nose'],
)
