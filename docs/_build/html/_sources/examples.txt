**********************
Examples and Use Cases
**********************


You can find fully functional examples in examples/ in the `repository <https://github.com/LoginRadius/Python-SDK>`_.

Accessing Raw Provider Data
---------------------------

If you do not want normalized data, but instead the raw return with respect to the provider, you must enable it.

.. code-block:: python

    #Let's get their first name but with the raw response from Facebook
    login = LoginRadius(token)
    login.user.profile.set_raw(True)
    print "Hello there," + login.user.profile['first_name']

.. warning::

    This will of course depend on the provider each user logs in with, and it is only recommended for advanced users
    where normalized data is not applicable.

    This will only set profile requests to raw, and not other attributes, such as status.


Preloading Data
---------------

To reduce load times, you probably don't want to make an external HTTP request while populating your templates. If you
know what data you need beforehand, we should fetch it.

First we should understand what happens in a a normal use case.

.. code-block:: python

    login = LoginRadius(token)

    #Your code here

    #This makes a GET request and will be blocking.
    print "Hello there," + login.user.profile['FirstName']

    #We already called profile, and all this data is already loaded into the dictionary.
    #This is non-blocking now.
    print "What can I do for you today, " + login.user.profile['FirstName'] + "?"

The first time you call any attribute will block and fetch the data remotely from LoginRadius. After doing so, it is
saved with respect to the attribute of our object.

However, this is not always optimal. You could call this in a thread and prepare the response in the meantime. While
threading is beyond the scope of this document, here is how you load the data preemptively.

.. code-block:: python

    login = LoginRadius(token)

    #Let's make sure the data is available to us.
    login.user.profile.load()

    #Your code here.

    #This makes a GET request and will be non-blocking now.
    print "Hello there," + login.user.profile['FirstName']

    #We already called profile, and all this data is already loaded into the dictionary.
    #This is non-blocking now.
    print "What can I do for you today, " + login.user.profile['FirstName'] + "?"


Invoking load on any user attribute will fetch the data.

Changing HTTP Libraries
-----------------------

By default, the requests module will be picked if it is version 2.0 or greater. However, you can override this and
change it as you see fit.

Checking current library after constructing a LoginRadius object.

.. code-block:: python

    login = LoginRadius(token)
    print login.settings.library

Changing the library for one LoginRadius object.

.. code-block:: python

    login = LoginRadius(token)

    #Let's opt in for urllib2 instead of requests
    login.change_library("urllib2")

Valid options are only 'urllib2' or 'requests'.

Changing the library for all future constructed LoginRadius objects.

.. code-block:: python

    from LoginRadius import LoginRadius

    #Changing to the urllib2 library
    LoginRadius.LIBRARY = "urllib2"


