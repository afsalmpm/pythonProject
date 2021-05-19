import os  # For storing sensitive data out of the code
import smtplib  # This is the email module in python
from email.message import EmailMessage  # This is to make python email messages more intuitive
import Xcel_files

file_path = Xcel_files.file_path
file1 = f'{Xcel_files.file1_name}.xlsx'
file2 = f'{Xcel_files.file2_name}.xlsx'

# The below details are saved in the system as Environment variables
FROM_EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
TO_EMAIL_ADDRESS = os.environ.get('TO_EMAIL')


# Attachment files below


def email_backup(date_of_backup):
    msg = EmailMessage()
    msg['Subject'] = f'Our backup on {date_of_backup}'
    msg['From'] = FROM_EMAIL_ADDRESS
    msg['To'] = TO_EMAIL_ADDRESS
    msg.set_content(f"Our backup on {date_of_backup}.\nThis email has been sent using Afsal's Python codes")

    files = [file1, file2]
    for file in files:
        with open(f'{file_path}{file}', 'rb') as f:
            file_data = f.read()
        msg.add_attachment(file_data, maintype='spreadsheet', subtype='xlsx', filename=file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# *************
# Test block
# **************
# transaction_date = '11/05/2021'
# email_backup(transaction_date)
