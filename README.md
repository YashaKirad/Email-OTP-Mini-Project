# Email-OTP-Mini-Project

# OTP Email Sender

This Python script demonstrates how to send a one-time password (OTP) email using Gmail's SMTP server. The script utilizes the `smtplib` library to establish a secure connection with the Gmail server and sends an OTP to the specified recipient's email address.

## How It Works

1. Import required libraries: `random` for generating random OTP and `smtplib` for sending emails using the Simple Mail Transfer Protocol.

2. Establish a connection with Gmail's SMTP server on port 587.

3. Start TLS (Transport Layer Security) security for secure communication.

4. Login to the Gmail account using the sender's email address and an app password.

5. Input the recipient's email address.

6. Generate a 4-digit OTP using the `random` library.

7. Compose the email message containing the OTP.

8. Send the email from the sender's email address to the recipient's email address.

9. Close the server connection.

## Usage

1. Make sure you have Python installed on your system.

2. Replace `'yashakirad@gmail.com'` with your Gmail email address and `'ynstcblzldrxbvaf'` with your Gmail app password.

3. Run the script.

4. Input the recipient's email address when prompted.

5. An OTP email will be sent to the recipient's email address.

## Note

- Ensure that you have enabled "Less secure app access" for the sender Gmail account if you're using your main Gmail account. Alternatively, you can use a separate Gmail account for this purpose.

- Make sure to keep your app password secure.

