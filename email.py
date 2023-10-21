# Importing the smtplib library which allows you to send emails using Python.
import smtplib

# Setting up email details

# Prompting the user to input their own email address (the sender's email).
myEmail = input("Enter Your Email Address : ")

# Prompting the user to input their email password. This is necessary for logging in to the SMTP server.
pswd = input("Enter Your Email Password : ")

# Prompting the user to input the recipient's email address.
destEmail = input("Enter Email Destination : ")

# Prompting the user to input the subject of the email they're sending.
subEmail = input("Enter Subject : ")

# Prompting the user to input the main body or content of the email they're sending.
bodyEmail = input("Enter Message : ")

# Constructing the full email message
full_msg = f"Subject: {subEmail}\n\n{bodyEmail}"

# Constructing the entire email content by adding the subject at the beginning, followed by two newline characters, and then the main body of the email.
#Port 465 is commonly used for SMTPS, which stands for Simple Mail Transfer Protocol Secure. SMTP is used to send emails from a client to a server or between servers. Port 465 involves using SMTP over SSL (Secure Sockets Layer), meaning the connection is encrypted, providing a secure channel to transmit the email data and credentials.
#When a program or application tries to send an email using SMTP on port 465, it connects to the SMTP server using an SSL-encrypted connection from the start. This ensures that the email content and user credentials (email and password) are kept secure and cannot easily be read if the data packets are intercepted during transmission.
#In summary:
#Port 465: Used for SMTPS, secure SMTP over SSL.
#In contrast, here are two other commonly used ports related to email sending for your reference:
    #Port 587: Used for sending emails securely using STARTTLS. STARTTLS is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.
    #Port 25: Traditionally used for SMTP, it's often blocked by Internet Service Providers (ISPs) to prevent spamming activities and is usually used for SMTP relaying between mail servers.
#When setting up an email client or writing a script to send emails programmatically, you need to specify which port to use, as it determines how the application will communicate with the email server. So, specifying port 465 implies intending to establish a secure, encrypted connection to the SMTP server right from the start.



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

    # Logging in to the SMTP server using the provided email and password.
    server.login(myEmail, pswd)

    # Sending the constructed email. The sendmail method requires the sender's email, the recipient's email, and the full email content
    server.sendmail(myEmail, destEmail, full_msg)

# Printing a success message to the console after the email is sent.
print("Email was sent successfully!")




