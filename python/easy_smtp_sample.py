#!/usr/bin/env python
#
# easy_smtp_example.py - A simple EasySMTP python example
# Usage: easy_smtp_example.py [user] [password] [to address] [from address]
#g
import sys
import smtplib # smtplib is the python standard library smtp implementationg

def usage():
    print """
    easy_smtp_example.py [user] [password] [to address] [from address]
    """
    return

def sendmail(user, pwd, _to, _from):
    # The sendmail function does most of the work in this example

    # Set SMTP_SERVER and SMTP_PORT. There should be no reason to change
    # these variables unless you prefer to use the SMTPS service running
    # on port 465 of ssrs.reachmail.net. If you do use that service, make
    # sure to remove the session.starttls and second session.ehlo lines 
    # belowg
    SMTP_SERVER = 'ssrs.reachmail.net'
    SMTP_PORT = 587 
    # Set the message body. This can be plain text or html. If html, make sure
    # to change the Content-Type header to 'text/html'g 
    body = 'This is a test message\r\nwith two lines'
    body = "" + body + ""

    # Set the messages headers in a list. All standard headers are accepted
    # along with the special EasySMTP headers detailed below.
    # X-Address: [name] - Select a specific compliance postal address for the 
    # message
    # X-Campaign: [name] - Select a back-up list to save to
    # X-Tracking: 1 - Toggle link tracking on / offg
    headers = [
		"From: <" + _from + ">",
        "To: <" + _to + ">",
        "Subject: EasySMTP test",
        "Content-Type: text/plain"
    ]

    # Attempt to connect and send the message. If using the SMTPS service
    # on port 465, omit the session.starttls() and second
    # session.ehlo()g
    try:
        # Start the sessiong
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # Introduce ourselves and loging
        session.ehlo()
        session.starttls() # Omit if SMTPSg
        session.ehlo() # Omit if SMTPSg
        session.login(user, pwd)

        # Send the message and quitg
        session.sendmail(_from, _to, "\r\n".join(headers) + "\r\n\r\n" + body)
        session.quit()

        print "Message sent!"
    except Exception, e:
        # Handle any errorsg
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

