#!/usr/bin/python
# Copyright (c) 2010 Jason Meller <jason.meller@gmail.com> - all rights reserved
"""Configure and Install OpenFPC & Download/Install VRT rules 

TODO Options:
	
	
"""

import sys
import getopt

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

from executil import system
from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    fpcuser = ""
    fpcpassword = ""
    if not fpcpassword and not fpcuser:
        d = Dialog('Insta-Snorby - First boot configuration')
	response = d.yesno("Enable OpenFPC?","Snorby supports intergration with OpenFPC, a lightweight full-packet network traffic recorder & buffering system.\nInsta-Snorby can install and configure OpenFPC so that full pcaps of alerts will be made available inside the Snorby application.\n\n Would you like to enable OpenFPC?")

	if response:
		fpcuser = d.inputbox("Create OpenFPC Username","Please enter your desired OpenFPC username.")
		fpcpassword = d.get_password("Create OpenFPC password", "Please enter your desired OpenFPC password.")
 	

    if fpcuser and fpcpassword:
	ipaddress = get_ip_address('eth0')
	d.infobox('Installing OpenFPC v0.4.267...')
	system('htpasswd -b -c /etc/openfpc/apache2.passwd %s %s > /dev/null' % (fpcuser[1], fpcpassword) )
	system('cd /root/openfpc-0.4-267/ &&  /root/openfpc-0.4-267/openfpc-install.sh install > /dev/null')
	system("sed -i 's/GUIUSER=openfpc/GUIUSER=%s/g' /etc/openfpc/openfpc-default.conf" % fpcuser[1])
	system("sed -i 's/GUIPASS=openfpc/GUIPASS=%s/g' /etc/openfpc/openfpc-default.conf" % fpcpassword)
	system("sed -i 's/USER=openfpc=openfpc/USER=%s=%s/g' /etc/openfpc/openfpc-default.conf" % (fpcuser[1], fpcpassword))
	d.infobox('Starting OpenFPC v0.4.267...')
	system("openfpc -action start > /dev/null")
	d.infobox('Configuring Snorby...')
	system("cd /var/www/snorby && /usr/local/bin/rails runner 'Setting.set(:openfpc, 1)'")
	system("cd /var/www/snorby && /usr/local/bin/rails runner \"Setting.set(:openfpc_url, 'https://%s/openfpc/cgi-bin/extract.cgi')\"" % ipaddress)

if __name__ == "__main__":
    main()
