#!/usr/bin/env python3

import argparse
import purestorage
import sys
import re

# Disable warnings using urllib3 embedded in requests or directly

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Script Options

argp = argparse.ArgumentParser()
argp.add_argument('-H', '--endpoint', required = True, help="FA hostname or ip address")
argp.add_argument('-a', '--apitoken', required = True, help="FA api_token")
argp.add_argument('-c', '--component', required = True,
                      help="FA hardware component/group name (For components CH0.BAY0, CH0.BAY1 etc the group name will be BAY")
argp.add_argument('-v', '--verbose', action='store_true',
                      help='increase output verbosity')
argp.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')
parser = argp.parse_args()

endPoint = parser.endpoint
apiToken = parser.apitoken
hwCompnt = parser.component
verbose = parser.verbose

# Getting all hardware component list

fa = purestorage.FlashArray(endPoint, api_token=apiToken)
fainfo = fa.list_hardware()

## Component status check - Start

allCompntStatus = {}

for compntInfo in fainfo:
    CompntName = compntInfo['name']

    if re.fullmatch('C[T,H]\d?\d?',hwCompnt) != None :

        if (hwCompnt[:2] in CompntName) and ("." not in CompntName):

            allCompntStatus[CompntName] = compntInfo['status']

    else:

        if hwCompnt in CompntName:
            allCompntStatus[CompntName] = compntInfo['status']

if verbose:
       for compntStatus in allCompntStatus:
            print("{:10} : {}".format(compntStatus,allCompntStatus[compntStatus]))

# Checking the provided component group exists

if len(allCompntStatus) == 0:
    print("[{}] No such component/group exists".format(hwCompnt))
    sys.exit(3)

isExit = "no"
for groupCompnt in allCompntStatus:

    if allCompntStatus[groupCompnt] not in ['ok', 'not_installed']:
        print("[{}] status is critical".format(groupCompnt))
        isExit = "yes"

if isExit == "yes":
    sys.exit(1)

print("[{}] component/group status is OK".format(hwCompnt))
sys.exit(0)

## Component status check - End
