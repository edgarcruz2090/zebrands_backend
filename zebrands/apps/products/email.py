import logging

import boto3

from django.conf import settings


class SesEmail:
    """Send a email with AWS SES"""

    def __init__(self, to, subject, html_content):
        self.to = to
        self.subject = subject
        self.html_content = html_content

    def send(self):
        try:
            ses_client = boto3.client(
                "ses",
                region_name=settings.SES_AWS_REGION,
                aws_access_key_id=settings.SES_AWS_ACCESS_KEY,
                aws_secret_access_key=settings.SES_AWS_SECRET_KEY,
            )
            response = ses_client.send_email(
                Source=settings.SES_AWS_SOURCE,
                Destination={"ToAddresses": self.to},
                Message={
                    "Subject": {
                        "Charset": "UTF-8",
                        "Data": self.subject,
                    },
                    "Body": {
                        "Html": {
                            "Charset": "UTF-8",
                            "Data": self.html_content,
                        }
                    },
                },
            )
            return response
        except Exception as e:
            logging.exception(f"Sending email: {e}")
