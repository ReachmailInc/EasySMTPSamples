using System;
using System.Net.Mail;

class SendViaES {
	public static void Main(String[] args) {
		string smtp_host = "ssrs.reachmail.net";
		int smtp_port = 587;
		string user = args[0];
		string pswd = args[1];
		string rcpt = args[2];
		string from = args[3];
		System.Net.ServicePointManager.ServerCertificateValidationCallback += (s, ce, ca, p) => true;
		System.Net.Mail.MailMessage Mail = new System.Net.Mail.MailMessage(from, rcpt);
		Mail.Subject = "CSHARP ES";
		Mail.Body = "CSHARP ES";
		System.Net.Mail.SmtpClient client = new System.Net.Mail.SmtpClient();
		client.Host = smtp_host; 
		client.Credentials = new System.Net.NetworkCredential(user, pswd);
		client.EnableSsl = true;
		client.Port = smtp_port; 
		client.Send(Mail);
	}
}
