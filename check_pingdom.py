#!/usr/bin/python

# This script made for Zabbix to check for Pingdom status on configured checks
# Created by Eric Harris (eric@itfargo.com)
# Grabs json results from Pingdom API call for a single check detail, returns current status

import requests, sys, getopt, json

def main(argv):
  # setup argument variables
  url = ''       # API base URL
  checkid = ''   # ID of the Pingdom check
  appkey = ''    # Pingdom application key
  username = ''  # Pingdom username
  password = ''  # Pingdom password
  try:
    # setup command line argument options
    opts, args = getopt.getopt(argv,"hu:i:k:a:p:")
  except getopt.GetoptError:
    # print usage guidelines if command line options are incorrect, then exit
    print 'check_pingdom -u <api-url> -i <check-id> -k <app-key> -a <pingdom-username> -p <pingdom-password>'
    sys.exit(2)
  for opt, arg in opts:
    # "help" option, to print usage
    if opt == '-h':
      print 'check_pingdom -u <api-url> -i <check-id> -k <app-key> -a <pingdom-username> -p <pingdom-password>'
      sys.exit()
    # sets "url" variable
    elif opt == '-u':
      url = arg
    # sets "checkid" variable
    elif opt == '-i':
      checkid = arg
    # sets "appkey" variable
    elif opt == '-k':
      appkey = arg
    # sets "username" variable ... "-a" is for "account"
    elif opt == '-a':
      username = arg
    # sets "password" variable
    elif opt == '-p':
      password = arg

  # sets "headers" variable for use in the API request
  headers = { 'App-Key': appkey }

  # makes the API request and stores json output in variable "r"
  r = requests.get(url + checkid, headers=headers, auth=(username,password))

  # parses json output in "r", stores in "checkjson"
  checkjson = json.loads(r.text)

  # returns only the Pingdom status of the requested check
  print(checkjson["check"]["status"])

if __name__ == "__main__":
  main(sys.argv[1:])
