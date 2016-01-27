#!/usr/bin/env perl
#
# easy_smtp_example.pl - A simple EasySMTP example
# easy_smtp_example.pl <user> <password> <to email> <from email>
#
# $Id$
# $Source$
#
use strict;
use warnings;
use Net::SMTP::TLS;

if (@ARGV < 4) {
	print "easy_smtp_example.pl <user> <password> <to email> <from email>\n";
	exit();
}

my $mailer = new Net::SMTP::TLS(
	'ssrs.reachmail.net',
	Hello => 'yourdomain.tld',
	Port => 25,
	User => $ARGV[0],
	Password => $ARGV[1],
	Debug => 1);
$mailer->mail($ARGV[3]);
$mailer->to($ARGV[2]);
$mailer->data;
$mailer->datasend("Subject: EasySMTP test\r\n\r\nTest message");
$mailer->dataend;
$mailer->quit;
exit();
