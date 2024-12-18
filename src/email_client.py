from __future__ import print_function
import time, os
from dotenv import load_dotenv
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Load the environment variables
load_dotenv()


class EmailWrapper:
    def __init__(
        self,
        sender_email,
        sender_name,
        to_email,
        to_name,
        cc_email,
        cc_name,
        bcc_email,
        bcc_name,
        reply_to_email,
        reply_to_name,
        html_content,
    ):
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.to_email = to_email
        self.to_name = to_name
        self.cc_email = cc_email
        self.cc_name = cc_name
        self.bcc_email = bcc_email
        self.bcc_name = bcc_name
        self.reply_to_email = reply_to_email
        self.reply_to_name = reply_to_name
        self.html_content = html_content
        self.configuration = sib_api_v3_sdk.Configuration()
        self.configuration.api_key["api-key"] = os.getenv("BREVO_API_KEY")

    # Define all the setter methods for the email wrapper
    def set_sender_email(self, sender_email):
        self.sender_email = sender_email

    def set_sender_name(self, sender_name):
        self.sender_name = sender_name

    # Come on now just give me all the setters
    def set_to_email(self, to_email):
        self.to_email = to_email

    def set_to_name(self, to_name):
        self.to_name = to_name

    def set_cc_email(self, cc_email):
        self.cc_email = cc_email

    def set_cc_name(self, cc_name):
        self.cc_name = cc_name

    def set_bcc_email(self, bcc_email):
        self.bcc_email = bcc_email

    def set_bcc_name(self, bcc_name):
        self.bcc_name = bcc_name

    def set_reply_to_email(self, reply_to_email):
        self.reply_to_email = reply_to_email

    def set_reply_to_name(self, reply_to_name):
        self.reply_to_name = reply_to_name

    # Define the method to send the email
    def send_email(self, subject, html_content: str):
        # send email
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(self.configuration)
        )
        sender = {"name": self.sender_name, "email": self.sender_email}
        to = [{"email": self.to_email, "name": self.to_name}]
        cc = [{"email": self.cc_email, "name": self.cc_name}] if self.cc_email else None
        bcc = (
            [{"email": self.bcc_email, "name": self.bcc_name}]
            if self.bcc_email
            else None
        )
        reply_to = {"email": self.reply_to_email, "name": self.reply_to_name}
        # headers = {"Test": "Hello World"}
        # params = {"parameter": "Param value", "subject": "Test Email - # 1"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            # headers=headers,
            html_content=html_content,
            sender=sender,
            subject=subject,
        )
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            raise e
