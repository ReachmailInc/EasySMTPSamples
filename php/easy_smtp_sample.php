<?php
 
// PHP has no native SMTP support, we recommend the SwiftMail library
// for adding SMTP support. http://swiftmailer.org/
require_once '/path/to/swift/lib/swift_required.php'; 
    
// Set message recipients
$send_to            = array(
                        'user1@domain.tld' => 'Bob Jones',
                        'user2@domain.tld' => 'Bob Smith,
                        'user3@domain.tld
                    );
    
// Set sender
$sent_from          = array(
                        'me@mydomain.tld' => 'Me'
                    );
 
// Set subject and body
$subject            = "Test message from EasySMTP";
$body               = "This is a test message.";

// Set SMTP connection details
$transport          = Swift_SmtpTransport::newInstance()
    ->setHost('ssrs.reachmail.net') // Host.  This should not need to change
    ->setPort(465) // Port.  Should not be changed as SwiftMail does not support starttls
    ->setUsername('accountid\\username')
    ->setPassword('Sup3rS3creT')
    ->setEncryption('ssl') // set the encription type.
    ;

// Create a Mailer
$mailer             = Swift_Mailer::newInstance($transport);

// Construct the message
$message            = Swift_Message::newInstance()
    ->setSubject($subject) // Set Subject line here
    ->setContentType('text/html') // Sets the Content-Type
    ->setFrom($sent_from) // Sets the sender address specified at the top
    ->setTo($send_to) // Sets the recipient addresses sprecified at the top
    ->setBody($body) // Sets the body of the email
    ;

// This method should be used to add addistional custom headers.
// Use the format: $headers->addTextHeader('X-Tracking', '1'); to set other 
// headers like X-Campaign or X-Address.
$headers = $message->getHeaders();  
$headers->addTextHeader('X-Tracking', '1');

// $result will be an integer representing the number of successful recipients
$result = $mailer->send($message);

print $result . "\n";
?>
