#!/usr/bin/python
import commands
import time
import json
import MySQLdb
from json import load
from urllib2 import urlopen

ip_sr = load(urlopen('http://jsonip.com'))['ip']
sql = "INSERT INTO latency (time,ip_sr,ip_ds,isp_ds,avgrtt) VALUES (%(time)s, %(ip_sr)s, %(ip_ds)s,%(isp_ds)s,%(avgrtt)s);"

def check_latency(k,v):
    print k
    result = commands.getoutput("fping -s -q -g %s -r 0" % k)
#    print result.splitlines()[-3].split(" ")[1]
    data = {
        "time": time.strftime("%m/%d/%Y %H:%M:%S"),
        "ip_sr":ip_sr,
        "ip_ds": k,
        "isp_ds":v,
        "avgrtt":float(result.splitlines()[-3].split(" ")[1])
    }
#    print data
#    print sql
    conn = MySQLdb.connect(host="localhost", user="***", passwd="***", db="***")
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

    # write to database

#    with open('/var/log/vccloudlatency.log', 'a') as outfile:
 #       json.dump(data, outfile)
  #      outfile.write('\n')
#if __name__ == "__main__":
#    for k,v in sorted(dict.items()):
#        check_latency(k,v)
