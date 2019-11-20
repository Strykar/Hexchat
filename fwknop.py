cat /home/strykar/.config/hexchat/fw.py
py exec import subprocess; subprocess.run('/usr/bin/ssh -T -i ~/.ssh/apu_fwknop_id_rsa root@apu.lan.wrtpoona.in &', shell = True)
#!/bin/python2
# -*- coding: UTF-8 -*-

#import socket
#from fko import *

#fko_port = 62201
#fko_host = "35.244.19.87"

#fko = Fko()
#fko.hmac_type(FKO_HMAC_SHA256)

#fko.spa_message('15.114.19.87,tcp/6697')
#fko.spa_data_final('RlHRCTCZ8aLvwYxSzksNlf1eIU6mx','')

#print "SPA Data:", fko.spa_data()
#print "Version:", fko.version()
#print "Timestamp:", fko.timestamp()
#print "Username:", fko.username()
#print "Digest Type (value):", fko.digest_type()
#print "Digest Type (string):", fko.digest_type_str()
#print "Digest:", fko.spa_digest()
#print "SPA Message:", fko.spa_message()

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.sendto(fko.spa_data(), (fko_host, fko_port))
#s.close()
