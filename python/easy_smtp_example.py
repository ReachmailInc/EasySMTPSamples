#!/usr/bin/env python
#
# easy_smtp_example.py - A simple EasySMTP python example
#
# $Id$
# $Source$
#
import sys, smtplib

def usage():
	print """
	easy_smtp_example.py <user> <password> <to address> <from address>
	"""
	return

def sendmail(user, pwd, _to, _from):
	SMTP_SERVER = 'ssrs.reachmail.net'
	SMTP_PORT = 25
	sender = _from
	rcpt = _to
	body = 'This is a test message'

	body = "" + body + ""
	headers = ["From: " + sender,
		"To: " + rcpt,
		"Subject: EasySMTP test",
		"Content-Type: text/plain"
	]

	try:
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(user, pwd)

		session.sendmail(sender, rcpt, "\r\n".join(headers) + "\r\n\r\n" + body)
		session.quit()
	except Exception, e:
		print "SMTP ERROR: %s" % e
		sys.exit(1)
	return True 

def run():
	if len(sys.argv) == 1:
		usage()
		sys.exit(0)
	if len(sys.argv) < 5:
		usage()
		sys.exit(1)
	sendmail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	sys.exit(0)

if __name__ == '__main__':
	run()
