****************
Reference Manual
****************

Data Points
-----------
When you access the python dictionary with respect to each attribute of the object, it is parsing the information
reflected in this document.

http://www.loginradius.com/datapoints

.. warning::
    These data points are subject to change and vary with providers.

For example

.. code-block:: python

    print login.user.profile['NickName']

May work for some providers like Mixi, but will not work for Facebook. Instead, you would get a key value error.

REST API
--------

You can take advantage of the raw API if you wish and learn how it works.

http://api.loginradius.com/help/


LoginRadius Object
------------------
.. automodule:: LoginRadius
    :members: