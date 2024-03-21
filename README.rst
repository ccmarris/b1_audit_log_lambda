============================================
Example AWS Lambda function call BloxOne API
============================================

| Version: 0.0.1
| Author: Chris Marrison
| Email: chris@infoblox.com

Description
-----------

Simple proof of concept code for an AWS Lambda function interacting with infoblox
BloxOne API. This proof of concept retrieves the bloxone audit log and returns
the raw JSON data when called.


Prerequisites
-------------

AWS Lambda Layer configured with: 

Python 3.11+
bloxone python module and dependencies

A sample layer is included in the *layers* directory of this project.


Basic Configuration
-------------------

The script utilise a b1.ini file to specify the API credentials.

Inifile configuration
---------------------

A sample inifile for the bloxone module is shared as *b1.ini* and follows
the following format provided below::

    [BloxOne]
    url = 'https://csp.infoblox.com'
    api_version = 'v1'
    api_key = '<you API Key here>'

You can therefore simply add your API Key, and this is ready for the bloxone


AWS Secrets Manager
~~~~~~~~~~~~~~~~~~~

For greater security the script should be modified to utilise the AWS
Secrets Manager. Once retrieved the credentials can be passed direct to 
the bloxone module as parameters. 

::
  class b1(builtins.object)
    b1(cfg_file='config.ini', api_key='', url='https://csp.infoblox.com', api_version='v1')



License
-------

This project is licensed under the 2-Clause BSD License
- please see LICENSE file for details.


Aknowledgements
---------------

Thanks to Jeff Cummings for bringing a real world requirement and giving
me a reason to publish this example.
