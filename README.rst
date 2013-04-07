Overview
========

doctest-ignore-unicode is a plugin (currently only for `Nose`_) that adds
a flag to ignore unicode literal prefixes in doctests.

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose

The implmentation is inspired by
https://github.com/nltk/nltk/blob/2and3/nltk/test/doctest_nose_plugin.py

Usage
=====

    >>> def hello_world():
    ...     return 'Hello World'
    >>> hello_world()  # doctest: +IGNORE_UNICODE
    u'Hello World'

FAQ
===

Why?
----

If you need to ask you probably don't need it.  (Hint: supporting python 2 & 3
in the same codebase).
