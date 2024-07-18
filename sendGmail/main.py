# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Set up the email parameters
# from_address = 'hasan84heydari@gmail.com'
# to_address = 'hasan84heydari@gmail.com'
# subject = 'Subject of the Email'
# body = 'Body of the email'

# # Create the MIMEMultipart message object
# msg = MIMEMultipart()
# msg['From'] = from_address
# msg['To'] = to_address
# msg['Subject'] = subject

# # Attach the email body to the message object
# msg.attach(MIMEText(body, 'plain'))

# # SMTP server configuration
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_user = from_address
# smtp_password = 'jzeh vxuf awtv jztm'  # or your app password if 2FA is enabled

# try:
#     # Connect to the SMTP server
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()  # Secure the connection

#     # Login to the SMTP server
#     server.login(smtp_user, smtp_password)

#     # Send the email
#     server.send_message(msg)

#     print('Email sent successfully!')

# except Exception as e:
#     print(f'Failed to send email: {e}')

# finally:
#     # Close the SMTP server connection
#     server.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email parameters
from_address = 'hasan84heydari@gmail.com'
to_address = 'hasan84heydari@gmail.com'
subject = 'Subject of the Email'
body = 'Body of the email'

# List of attachment file paths
file_paths = []
root = "D:\Programming\Code\Goshadi\convertZip"
entries = os.listdir(root)
for entry in entries:
  if (entry.endswith("zip")):
      file_paths.append(root + '\\' + entry)

# Create the MIMEMultipart message object
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

# Attach the email body to the message object
msg.attach(MIMEText(body, 'plain'))

# Attach multiple files to the email
for file_path in file_paths:
    with open(file_path, 'rb') as attachment:
        # Create a MIMEBase object
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

        # Encode the file in base64
        encoders.encode_base64(part)

        # Add header to the attachment
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(file_path)}',
        )

        # Attach the MIMEBase object to the email
        msg.attach(part)

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = from_address
smtp_password = 'jzeh vxuf awtv jztm'  # Replace with your app password

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection

    # Login to the SMTP server
    server.login(smtp_user, smtp_password)

    # Send the email
    server.send_message(msg)

    print('Email sent successfully!')

except Exception as e:
    print(f'Failed to send email: {e}')

finally:
    # Close the SMTP server connection
    server.quit()
