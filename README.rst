mnlp
=====

.. image:: https://travis-ci.com/byam/mnlp.svg?branch=master
:target: https://travis-ci.com/byam/mnlp

MNLP: Mongolian Natural Language Processing.

https://pypi.org/project/mnlp/


Install
----------------------

.. code-block:: console

    $ pip install mnlp

Usage
----------------------

- Example: Stopwords

.. code-block:: python

    import mnlp

    print(mnlp.stopwords.words())
    # >> ['нь', 'ч', 'л', 'ба']

- Testing
.. code-block:: console

    $ python -m unittest discover

License
----------------------
MIT
