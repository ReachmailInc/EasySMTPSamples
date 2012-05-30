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

if (@ARGV < 5) {
	print "easy_smtp_example.pl <user> <password> <to email> <from email>";
	exit();
}

my $mailer = new NEW::SMTP::TLS(
	'ssrs.reachmail.net',
	Hello => 'ssrs.reachmail.net',
	Port => 25,
	User => $ARGV[1],
	Password => $ARGV[2]);
$mailer->mail($ARGV[4]);
$mailer->to($ARGV[3]);
$mailer->data;
$mailer->datasend("Subject: EasySMTP test\r\n\r\nTest message");
$mailer->dataend;
$mailer->quit;
exit();
