#!/usr/bin/env python3

import argparse
import subprocess
import datetime
from pytz import timezone
import time
import sys

parser = argparse.ArgumentParser(description='Icinga plugin to check the time on a server using SNMP.')
parser.add_argument('-H', '--hostname', required = True, help='Name or IP address of host to check.')
parser.add_argument('-C', '--community', required = True, help='Community name for the host\'s SNMP agent (implies SNMP v1 or v2c with option)')
parser.add_argument('-S', '--snmpver', default="2c", help='Version of SNMP protocol to use: 1|2c|3. (Default: 2c)')
parser.add_argument('-w', '--warn', default=30, type=int, help='Number of seconds the time can be off before giving warning alert. (Default: 30)')
parser.add_argument('-c', '--critical', default=60, type=int, help='Number of seconds the time can be off before giving critical alert. (Default: 60)')
parser.add_argument('-p', '--port', default=161, type=int, help='SNMP port of remote server')
parser.add_argument('-Z', '--timezone', required = True, help='Timezone of the remote host.  This is necessary, because Windows hosts don\'t report the timezone.')
parser.add_argument('-d', '--debug', action='store_true', help='Print extra debugging information (for console usage only)')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

snmp_community = args.community
remote_host = args.hostname
snmp_port = args.port
snmp_ver = args.snmpver
remote_tz = args.timezone
critical_limit = args.critical
warning_limit = args.warn
verbose = args.debug

OID_hrSystemDate=".1.3.6.1.2.1.25.1.2"

try:
   subprocess.check_output(["/usr/bin/snmpwalk", "-r", "3", "-c", "{}".format(snmp_community), "-v", "{}".format(snmp_ver), "{}:{}".format(remote_host,snmp_port), "{}".format(OID_hrSystemDate)])
except subprocess.CalledProcessError as e:
   print(e.output.decode())
   sys.exit(3)

# Finding remote time
snmp_remote_ts = subprocess.run(["/usr/bin/snmpwalk", "-r", "3", "-c", "{}".format(snmp_community), "-v", "{}".format(snmp_ver), "{}:{}".format(remote_host,snmp_port), "{}".format(OID_hrSystemDate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
remote_time = snmp_remote_ts.stdout.decode().split()[-1].replace(","," ").split(".")[0]
remote_ts = datetime.datetime.strptime(remote_time, "%Y-%m-%d %H:%M:%S")

if verbose:
   print("/usr/bin/snmpwalk -r 3 -c {} -v {} {}:{}".format(snmp_community,snmp_ver,remote_host,snmp_port))
   print("Remote server time: {}".format(snmp_remote_ts))

# Finding actual time of provided timezone
actual_time_now = datetime.datetime.now(timezone(remote_tz)).replace(tzinfo=None,microsecond=0)

# Finding time difference
time_diff = actual_time_now - remote_ts
time_diff_seconds = time_diff.seconds

if verbose:
   print("Remote server {} time now: {}".format(remote_host,remote_ts))
   print("{} time now: {}".format(remote_tz,actual_time_now))
   print("Time difference: {}".format(time_diff_seconds))

if time_diff_seconds > critical_limit:
   print("CRITICAL - {} time is off by {} seconds!".format(remote_host,time_diff_seconds))
   sys.exit(2)

elif time_diff_seconds > warning_limit:
   print("WARNING - {} time is off by {} seconds!".format(remote_host,time_diff_seconds))
   sys.exit(1)

else:
   print("OK - {} time differs by {} seconds".format(remote_host,time_diff_seconds))
   sys.exit(0)
