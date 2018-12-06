<?php

require_once '/PathToSwiftModule/lib/vendor/autoload.php';

$message_content = file_get_contents('/Path/To/HtmlContent/msg.htm');

// Set message recipients
$send_to            = array(
                        'email@domain.tld' => 'Recipient Name'
                    );
    
// Set sender
$sent_from          = array('email@domain.tld' => 'From Name');
// Set subject and body
$subject            = "Attachment Test 1";
$body = $message_content;

// Set SMTP connection details
$transport          = (new Swift_SmtpTransport('ssrs.reachmail.net', 587, 'tls'))
    ->setUsername('USERNAME')
    ->setPassword('PASSWORD')
    ;

// Create a Mailer
$mailer             = new Swift_Mailer($transport);
// SMTP logging (optional but very handy when needed)
$logger = new Swift_Plugins_Loggers_EchoLogger();
$mailer->registerPlugin(new Swift_Plugins_LoggerPlugin($logger));

// Construct the message
$message            = (new Swift_Message($subject))
    ->setFrom($sent_from)
    ->setContentType('text/html')
    ->setTo($send_to)
    ->setBody($body)
    ;
$message->attach(Swift_Attachment::fromPath('/Path/To/Attachment/Location/'));
$headers = $message->getHeaders();
//$headers->addTextHeader('x-dkim-options', 's=k1; i=FromEmail@domain.tld'); //optional DKIM key signing header. 

// $result will be an integer representing the number of successful recipients

 $result = $mailer->send($message);
print $result . "\n";

?>
