#!/usr/bin/env python3

import sys
import ipaddress
import subprocess


try:

   getIP = ipaddress.ip_address(input("Provide an IP address: "))
   print("")

except:
   print("Not a valid IP address")
   sys.exit(3)


if getIP.is_private == False:
    reverseIP = getIP.reverse_pointer.rstrip('.in-addr.arpa')

else:
	print("Not a public IP")

rblNames = open('rblnames.db','r')

for rblName in rblNames:

    result = subprocess.run(["nslookup", "{}.{}".format(reverseIP,rblName.strip())], capture_output=True, text=True)

    if "Non-authoritative answer" in result.stdout:
        print("Listed on: {}".format(rblName))

    else:
        print("NOT Listed on: {}".format(rblName))

rblNames.close()
