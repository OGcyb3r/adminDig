#!/usr/bin/env python3.6
#
# find a path of website 2020/05/22
#
import sys, os, time, http.client
import socket
import socks
from datetime import datetime

def d2():
    today = datetime.today()
    d2 = today.strftime("%a %H:%M:%S %m/%d/%Y ")
    return(d2)

clearxc='clear'
os.system(clearxc)
if len(sys.argv) <= 2:
	print(("""
     ██          ██             ██          ███████   ██
    ████        ░██            ░░          ░██░░░░██ ░░   █████
   ██░░██       ░██ ██████████  ██ ███████ ░██    ░██ ██ ██░░░██
  ██  ░░██   ██████░░██░░██░░██░██░░██░░░██░██    ░██░██░██  ░██
 ██████████ ██░░░██ ░██ ░██ ░██░██ ░██  ░██░██    ░██░██░░██████
░██░░░░░░██░██  ░██ ░██ ░██ ░██░██ ░██  ░██░██    ██ ░██ ░░░░░██
░██     ░██░░██████ ███ ░██ ░██░██ ███  ░██░███████  ░██  █████
░░      ░░  ░░░░░░ ░░░  ░░  ░░ ░░ ░░░   ░░ ░░░░░░░   ░░  ░░░░░
\x1b[1;38;5;255m
[\x1b[1;38;5;180m + \x1b[0m\x1b[1;38;5;255m] Result saved to websites/ folder
[\x1b[1;38;5;180m + \x1b[0m\x1b[1;38;5;255m] works on py3.6
[\x1b[1;38;5;180m + \x1b[0m\x1b[1;38;5;255m] No http or https

\x1b[1;38;5;155m-t\x1b[0m\x1b[1;38;5;255m scan with tor connection\x1b[0m\x1b[1;38;5;255m
\x1b[1;38;5;155m-x\x1b[0m\x1b[1;38;5;255m scan without tor connection\x1b[0m
python3.6 admindig.py target.com \x1b[1;38;5;155m-t\x1b[0m
python3.6 admindig.py target.com \x1b[1;38;5;155m-x\x1b[0m
  \n\n\n"""))
	sys.exit(1)
site = sys.argv[1].replace("https://","").rsplit("/",1)[0]
site = site.lower()
path = "websites/%s"%(site)
os.makedirs("%s"%path, exist_ok=True)
if sys.argv[2] == '-t':
	setHdr="ON"
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
	socket.socket = socks.socksocket
elif sys.argv[2] == "-x":
	setHdr="OFF"
	pass
admin_path = open('adminpath.txt', 'r')
print(("""[\x1b[1;38;5;156m + \x1b[0m] Tor is %s
[\x1b[1;38;5;156m + \x1b[0m] Result saved : websites/%s/result.txt
[\x1b[1;38;5;156m + \x1b[0m] %s"""%(setHdr,site,d2())))
time.sleep(0.5)
print(("""\x1b[1;38;5;120mStarting \x1b[0m..."""))
try:
	for admin in admin_path:
		admin = admin.replace("\n","")
		admin = "/" + admin
		connection = http.client.HTTPSConnection(site)
		connection.request("GET", admin)
		r1 = connection.getresponse()
		file = open("websites/%s/result.txt"%(site), "a+")
		file.write("[ %s %s ] %s%s\n" %(r1.status,r1.reason,site,admin))
		file.close()
		if r1.status == 200:
			print("[\x1b[1;38;5;10m",r1.status,r1.reason,"\x1b[0m] \x1b[1;38;5;255m%s%s\x1b[0m"%(site,admin))
		elif r1.status == 301:
			print("[\x1b[1;38;5;244m",r1.status,r1.reason,"\x1b[0m] \x1b[37;38;5;241m%s%s\x1b[0m"%(site,admin))
		else:
			print("[\x1b[1;38;5;244m",r1.status,r1.reason,"\x1b[0m] \x1b[37;38;5;241m%s%s\x1b[0m"%(site,admin))
except(KeyboardInterrupt,SystemExit):
		raise
except:
		pass
