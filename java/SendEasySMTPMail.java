/**
 * Sending email programmatically using JSP and Java
 */
package mail;   //add your own package designator
import javax.mail.*;
import javax.mail.internet.*;
import java.util.*;


/**
 * The Class SendEasySMTPMail.
 *
 * @author developer
 * 
 * Be sure to import javax.mail.jar into you lib directory or anywhere in your classpath
 * and alter your BuildPath properties to add the jars. Depending on your version of Java
 * and javax.mail.jar, you may need to add the javax.annotation.jar as well.
 */
public class SendEasySMTPMail {

	/** The from_email. */
	static String from_email = "no-reply@myDomain.com";
	
	/** The user name. */
	private static String userName ="Put Account Id here\\admin";
	
	/** The acct_pwd. */
	private static String acct_pwd = "change to your password";
	
	/** The smtp_host. */
	private static String smtp_host = "ssrs.reachmail.net";
	
	/** The use_port. */
	public static String use_port  = "465";
	
	/** The to_addr. */
	public static String to_addr = "email"; //just initializing here
	
	/** The subject. */
	public static String subject = "Login Credentials";  // You can put any subject here
	
	/** The msg_text. */
	public static String msg_text = "Hello. You have just been signed up to log into my website. Thanks. ";
	
	/** The socket factory class. */
	private static String socketFactoryClass = "javax.net.ssl.SSLSocketFactory";

	/**
	 * Sets the up and send.
	 *
	 * @param emailAddressofRecipient the new up and send
	 */
	public static boolean setupAndSend(String emailAddressofRecipient)
	{
		boolean success;
		to_addr= emailAddressofRecipient;
		success = sendMail(); 
		return success;
	}


	/**
	 * Send mail.
	 *
	 * @return true, if successful
	 */
	public synchronized static boolean sendMail(){

		Properties props = new Properties();
		props.put("mail.smtp.user", userName);
		props.put("mail.smtp.host", smtp_host);
		props.put("mail.smtp.port", use_port);
		props.put("mail.smtp.starttls.enable","true");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.ssl.enable", "true");
		props.put("mail.smtp.debug", "false");         
		props.put("mail.smtp.socketFactory.port", use_port);
		props.put("mail.smtp.socketFactory.class", socketFactoryClass);
		props.put("mail.smtp.socketFactory.fallback", "false");

		try
		{
			Session session = Session.getDefaultInstance(props, null);
			session.setDebug(false);
			MimeMessage msg = new MimeMessage(session);
			msg.setText(msg_text);
			msg.setSubject(subject);
			msg.setFrom(new InternetAddress(from_email));
			msg.addRecipient(Message.RecipientType.TO, new InternetAddress(to_addr));


			msg.saveChanges();
			Transport transport = session.getTransport("smtp");
			transport.connect(smtp_host, userName, acct_pwd);
			transport.sendMessage(msg, msg.getAllRecipients());
			transport.close();
			return true;
		}
		catch (Exception e)
		{
			e.printStackTrace();
			System.out.println(e.toString());
			return false;
		}
	}


}
