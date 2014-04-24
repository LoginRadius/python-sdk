****************
Quickstart guide
****************

This guide should help you install and utilize LoginRadius and its feature set quickly and painlessly.
For more examples, please see examples.

Install
-------

Prerequisites
=============

You will need at least Python - 2.7 or greater. LoginRadius module utilizes the `namedtuple
<https://docs.python.org/2/library/collections.html#collections.namedtuple>`_ from the collections library and the
`import_module <https://docs.python.org/2/library/importlib.html>`_ from importlib.

From Package
============

Using pip

.. code-block:: bash

    pip install loginradius

or with easy_install

.. code-block:: bash

    easy_install loginradius

From Source
===========

You can download the latest version from `PyPI <https://pypi.python.org/pypi/LoginRadius/2.0>`_

- Unzip/untar the files.
- Browse to the directory that you extracted the files to.
- Run:

.. code-block:: bash

    python setup.py install

To install the LoginRadius module.

Using the LoginRadius Object
----------------------------

import the class

.. code-block:: python

    from LoginRadius import LoginRadius

When you initialise your application, you will need to set your API Secret. This can be found in your
control panel under your dashboard:

https://secure.loginradius.com/account#dashboard

When your Python application first starts up, you should set your API Secret once and only once

.. code-block:: python

    LoginRadius.API_SECRET = "some-really-obscure-string"

When you receive a callback from LoginRadius after a user has authenticated with their provider it will come with a
token parameter. For example, with python in CGI we can do:

.. code-block:: python

    import cgi
    arguments = cgi.FieldStorage()
    token = arguments.getvalue('token')

This is highly dependent on your framework. You should browse some of our :doc:`examples` for one that fits with your web
framework and code flow.

We can now construct a LoginRadius object with respect to this token.

.. code-block:: python

    login = LoginRadius(token)

Doing so will make an HTTP request to LoginRadius for the access token. Not to be confused with the token we just
received from our callback. This new token is the basis for all API calls to LoginRadius.

With our newly constructed object, we can perform any API call listed in the online API help document. As long as
your plan is setup to do so! For example, the basic profile data is available to anyone.

http://api.loginradius.com/help/

We can access the profile information from the login object as a namedtuple.

.. code-block:: python

    if login.access.valid():
        print ("Hello there, " + login.user.profile["FirstName"] + ".")

We first check to see if our token hasn't expired. Be wary that storing a LoginRadius object for too long may cause
the token to become invalid. The default time, at the time of writing this guide, is fifteen
minutes.

The next line of code embedded in the if statement prints the user's first name.

This data is normalized across all data providers and is stored as a python dictionary to adapt to the API if changes
are made at a later date. To view all up to date items available to you in the dictionary, visit:

http://www.loginradius.com/datapoints/

The thought process behind the LoginRadius object is to provide easily accessible functions with minimal arguments.
It only loads data when needed.

Breaking Down the LoginRadius Object
------------------------------------

Like our previous example, profile is not the only attribute available to you.

.. py:attribute:: api

    This should only be used in cases where you want direct access to the LoginRadiusAPI object without our wrapper.
    It is highly advised against using this attribute at all.

    The api attribute is class of: :class:`LoginRadius.LoginRadiusAPI`

.. py:attribute:: access

    Contains useful information about the access token.

    .. py:attribute:: expire

        A string containing the date when this access token is no longer valid.

    .. py:attribute:: raw

        A dictionary containing the raw JSON response from LoginRadius for the token.

    .. py:attribute:: token

        This is our access token. Essentially for every API call.

    .. py:method:: valid()

        Invoking this will return a True or False boolean for if the access token is still valid. It is useful to check
        before making an API call. This method will only compare the stored expired attribute date and current UTC time.
        It will not make a remote call to the server to validate.


.. py:attribute:: error

    A string of the last error message encountered.

.. py:attribute:: settings

    HTTP library settings for encoding requests.

    .. py:attribute:: library

        Stores a string of the HTTP library currently being used with the LoginRadius object. Currently, this value
        can either be 'urllib2' or 'requests'. Please call _settings(library) and not this if you intend to change it.

    .. py:attribute:: urllib

        imported module of urllib.

    .. py:attribute:: urllib2

        imported module of urllib2.

    .. py:attribute:: json

        imported module of json.

    .. py:attribute:: requests

        imported module of requests

.. py:attribute:: token

    The original token from the callback.

.. py:attribute:: user

     Some of these attributes may not pull any data. Please check your endpoints at
     http://www.loginradius.com/datapoints/

     All of these attributes, by default, set raw=False to normalize data.

    .. py:attribute:: profile

        Information from the user's profile with respect to the current provider.

    .. py:attribute:: photo

        Photos with regards to the album_id attribute.

        .. py:attribute:: album_id

            A string of the album_id to be set before retrieval.

    .. py:attribute:: check_in

        Get a list of checked in places from this profile.

    .. py:attribute:: album

        Get a list of albums available on this profile.

    .. py:attribute:: audio

        Get a list of audio available on this profile.

    .. py:attribute:: video

        Get a list of uploaded videos on this profile

    .. py:attribute:: contacts

        Get a list of contacts, you can also specify a next_cursor attribute.

        .. py:attribute:: next_cursor

            An optional string for the next cursor.

    .. py:attribute:: status

        Get a list of status updated on this profile.

    .. py:attribute:: group

        Get a list of groups from this profile.

    .. py:attribute:: event

        Get a list of events from this profile.

    .. py:attribute:: mention

        Get a list of mentions from this profile.

    .. py:attribute:: activity

        Get a list of activities from this profile.

    .. py:attribute:: following

        Get a list of following from this profile.

    .. py:attribute:: page

        Get page data with respect to what this user's profile can see.

        .. py:attribute:: page_name

            A string containing the unique identifier for the page to fetch data from.

    .. py:attribute:: like

        Get a list of likes from this profile.

    .. py:method:: status_update(status, title='', url='', imageurl='', caption='', description='')

        Perform a status update on the profile on behalf of the user.
        Some of these arguments may be ignored depending on the provider.

    .. py:method:: direct_message(to, subject, message)

        Direct message another user on behalf of this user.