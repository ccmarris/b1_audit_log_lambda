#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
------------------------------------------------------------------------

 Description:
  Lookup query against TIDE active state and historic data
  producing basic report on whether there is active/historical
  data with simplified report output.

  For more extensive output for a specific IOC use tide-lookup.py

 Requirements:
  Requires bloxone

 Author: Chris Marrison

 Date Last Updated: 20240301

Copyright 2024 Chris Marrison / Infoblox

Redistribution and use in source and binary forms,
with or without modification, are permitted provided
that the following conditions are met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

------------------------------------------------------------------------
"""
__version__ = '0.0.1'
__author__ = 'Chris Marrison'

import boto3
import datetime
import json
import logging
import os
import time
import bloxone

# ** Functions **


def clean_up_message(message):
    '''
    '''
    json_dumps_cleanup = { '\"': '', '\\n': '\n' }
    for key, value in json_dumps_cleanup.items():
        message = message.replace(key, value)
    
    return message


def auth(event):
    '''
    Verify Request
    '''
    authorised = False
    ignore_timestamp = False
    
    '''
    Perform some form of authentication and return True is successful

    Using X-Auth header for proof of concept, but this could be an api_key
    or aws credentials
    '''
    headers = event.get('headers')
    # Check for test header
    if headers.get('X-Auth') == 'infoblox-cribl':
        authorised = True
    else:
        authorised = True    

    return authorised
    

def lambda_handler(event, context):
    # TODO implement
    message = {}
    success = False
    client = boto3.client('lambda')

    if auth(event):
        
        b1 = bloxone.b1platform('b1.ini')
        response = b1.auditlog(_limit='100')
        success = True
        message = json.dumps(response)
        
    else:
        success = False
        message = { "authentication": "Not authorised" }
        message = json.dumps(message)
  
    
    if success:
        status = 200
    else:
        status = 401
    
    #url = params['response_url']
    #body = post_response(url, message)
    
    return {
        'statusCode': status,
        'Content-Type': 'application/json',
        'body': message
    }

    