**********
Exceptions
**********

Handling Exceptions
-------------------

A list of specific exceptions are in :class:`LoginRadius.Exceptions`

However, there is a catch all class from which all LoginRadius exceptions inherit from.
:class:`LoginRadius.LoginRadiusExceptions`

.. code-block:: python

    from LoginRadius import LoginRadiusExceptions

    try:
        print login.user.profile['FirstName']

    except LoginRadiusExceptions:
        print "Something went wrong!"
        print login.error

The error attribute to your LoginRadius object contains a string that may help you solve why this exceptions was
raised in the first place.