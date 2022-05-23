# rbl_check

## SYNOPSIS

```sh
rbl_check <IP Address>
```

## DESCRIPTION

**[rbl_check](https://github.com/nijeshnalan/python-scripts/blob/master/rbl-check/rbl_check)** is a command line tool that checks a mail server IP address against over 80 DNS based email blacklists. This script prints the listed RBLs with respective delist URL. 

**[rblInfo.db](https://github.com/nijeshnalan/python-scripts/blob/master/rbl-check/rblInfo.db)** This file contains the details of the RBLs. 

**This commandline tool checks the IP against the following RBLs:**

|    |    |    |
| ------ | ------ | ------ |
| z.mailspike.net | rep.mailspike.net | bl.mailspike.net | 
| safe.dnsbl.sorbs.net | spam.dnsbl.sorbs.net | recent.spam.dnsbl.sorbs.net |
| problems.dnsbl.sorbs.net | old.spam.dnsbl.sorbs.net | new.spam.dnsbl.sorbs.net | 
| socks.dnsbl.sorbs.net | relays.dnsbl.sorbs.net | smtp.dnsbl.sorbs.net |
| proxies.dnsbl.sorbs.net | block.dnsbl.sorbs.net | dnsbl.sorbs.net | 
| dul.dnsbl.sorbs.net | web.dnsbl.sorbs.net | zombie.dnsbl.sorbs.net |
| aspews.ext.sorbs.net | escalations.dnsbl.sorbs.net | http.dnsbl.sorbs.net 
| l4.bbfh.ext.sorbs.net | misc.dnsbl.sorbs.net | xbl.spamhaus.org |
| zen.spamhaus.org | pbl.spamhaus.org | sbl.spamhaus.org | 
| cbl.abuseat.org | truncate.gbudb.net | ips.backscatterer.org |
| dnsbl.justspam.org | dnsbl-1.uceprotect.net | dnsbl-2.uceprotect.net |
| dnsbl-3.uceprotect.net | black.junkemailfilter.com | hostkarma.junkemailfilter.com |
| bl.spamcop.net | all.s5h.net | rbl.interserver.net | 
| exploit.mail.abusix.zone | black.mail.abusix.zone | dyna.spamrats.com |
| all.spamrats.com | spam.spamrats.com | noptr.spamrats.com | 
| dnsbl.dronebl.org | bl.score.senderscore.com | 0spam.fusionzero.com |
| backscatter.spameatingmonkey.net | bl.spameatingmonkey.net | bl.blocklist.de | 
| bl.konstant.no | bl.nosolicitado.org | bl.worst.nosolicitado.org |
| bl.suomispam.net | dnsbl.net.ua | dnsbl.spfbl.net | 
| fnrbl.fast.net | netscan.rbl.blockedservers.com | spam.rbl.blockedservers.com |
| rbl.blockedservers.com | rbl.abuse.ro | rbl.dns-servicios.com | 
| rbl2.triumf.ca | spam.dnsbl.anonmails.de | spam.pedantic.org |
| spamrbl.imp.ch | mail-abuse.com | torexit.dan.me.uk | 
| bl.scientificspam.net | dnsbl.zapbl.net | access.redhawk.org |
| b.barracudacentral.org | bb.barracudacentral.org | bl.drmx.org | 
| bl.rbl.scrolloutf1.com | cart00ney.surriel.com | psbl.surriel.com |
| db.wpbl.info | dnsbl.kempt.net | dnsbl.tornevall.org | 
| dnsrbl.swinog.ch | ix.dnsbl.manitu.net | mail-abuse.blacklist.jippg.org |
| multi.surbl.org | spamlist.or.kr | spamsources.fabel.dk | 

## BUGS

Please report them at: [https://github.com/nijeshnalan/python-scripts/issues](https://github.com/nijeshnalan/python-scripts/issues)

## AUTHOR

Nijesh Nalan \<<nijesh.n@grepitout.com>\>
