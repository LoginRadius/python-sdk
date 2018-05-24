LoginRadius offers a complete social infrastructure solution combining 30 major social platforms into one unified API.
With LoginRadius, websites and mobile apps can integrate social login, enable social sharing, capture user profiles and
social data, create a single sign-on experience for their users, and get comprehensive social analytics.
Our social solution helps websites engage, understand, and leverage their users.

This module provides a wrapper for urllib2 or the requests library to easily access the API from
https://docs.loginradius.com/ in a more "pythonic" way. Providing easier access to essential data in a few lines of code.
This will work with 2.0 API specifications.

For more information, visit: http://loginradius.com/

Prerequisites
========

You will need at least Python - 2.7 or greater. LoginRadius module utilizes the namedtuple from the collections library
and the import_module from importlib.

From Package
=========

Using pip

pip install loginradius-v2

or with easy_install

easy_install loginradius-v2

Changelog
======
3.1.0
-----

* Passed Api key and Secret key in herader for management API's.
* Passed SOTT In header.
* Added Configuration API
* Added Management API to generate a SOTT.
* Implemented ability to support proxy server.
* Supported NULL and projection in fields.
* Added new V2 API's.


3.0
-----

* Added Latest V2 APIs.