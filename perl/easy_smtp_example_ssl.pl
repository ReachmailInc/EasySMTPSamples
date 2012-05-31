#!/usr/bin/env perl
#
# easy_smtp_example_ssl.pl - A simple EasySMTP example that uses the SMTPS
# service at ssrs.reachamil.net:465
#
use warnings;
use strict;
use Net::SMTP::SSL;

if (@ARGV < 4) {
	die "easy_smtp_example_ssl.pl <user> <passwd> <to email> <from email>\n";
}

my $user = $ARGV[0];
my $passwd = $ARGV[1];

my $smtps = Net::SMTP::SSL->new('ssrs.reachmail.net',
	Port => 465,
	SSL_version => 'SSLv3:!SSLv2') or warn "$!\n";

defined ($smtps->auth($user, $passwd))
	or die "Can't authenticate: $!\n";

$smtps->mail($ARGV[4]);
$smtps->to($ARGV[3]);
$smtps->data();
$smtps->datasend("To: $ARGV[3]\r\n");
$smtps->datasend("From: $ARGV[4]\r\n");
$smtps->datasend("Subject: EasySMTP test message\r\n");
$smtps->datasend("Content-Type: text/plain\r\n\r\n");
$smtps->datasend("This is a test message\r\n");
$smtps->dataend();
$smtps->quit();

__END__
