import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import environment


class EmailManager:
    def __init__(self):
        self.sender_email = environment.EMAIL_SENDER
        self.password = environment.EMAIL_PASSWD

    def email_collaborator(self, doc_title=None, email=None, email_type=None):
        """
            Send an email to the collaborator based on the email_type
        """
        if (environment.ENABLE_EMAIL == 1):

            message = MIMEMultipart("alternative")
            message["From"] = self.sender_email
            message["To"] = email

            # Banned Collaborator
            if email_type == 'ban':
                message["Subject"] = "IReNE: Banned Collaborator - DO NOT REPLY TO THIS EMAIL"
                html = """\
                    <html>
                      <body>
                        <p>Hello from IReNE Administrator,<br><br>
                            The collaborator access for your <strong>IReNE: Tell Space</strong> account has been banned. 
                            <br><br>All documents created by this account will be set to unpublished for security purposes.
                            
                            Please contact system administrators for any misunderstandings.
                        </p>
                      </body>
                    </html>
                    """
                message.attach(MIMEText(html, "html"))

            # Unban Collaborator
            elif email_type == 'unban':
                message["Subject"] = "IReNE: Access Reestablished - DO NOT REPLY TO THIS EMAIL"
                html = """\
                    <html>
                      <body>
                        <p>Hello from IReNE Administrator,<br><br>
                            The collaborator access for your <strong>IReNE: Tell Space</strong> has been reestablished.
                            All documents related to this account will be set to published. 
                            <br><br>Please contact system administrators for any misunderstandings.
                        </p>
                      </body>
                    </html>
                    """
                message.attach(MIMEText(html, "html"))

            # Document published
            elif email_type == 'publish':
                message["Subject"] = "IReNE: Republished Document - DO NOT REPLY TO THIS EMAIL"
                html = f"""\
                            <html>
                              <body>
                                <p>Hello from IReNE Administrator,<br><br>
                                    The document with title <strong>"{doc_title}"</strong> has been republished.
                                    Please contact system administrators for any misunderstandings.
                                </p>
                              </body>
                            </html>
                            """
                message.attach(MIMEText(html, "html"))

            # Document Unpublished
            elif email_type == 'unpublish':
                message["Subject"] = "IReNE: Unpublished Document - DO NOT REPLY TO THIS EMAIL"
                html = f"""\
                            <html>
                              <body>
                                <p>Hello from IReNE Administrator,<br><br>
                                    The document <strong>"{doc_title}"</strong> has been unpublished.
                                    Please contact system administrators for any misunderstandings.
                                </p>
                              </body>
                            </html>
                            """
                message.attach(MIMEText(html, "html"))

            else:
                raise Exception('Unable to send email.')

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, email, message.as_string())
                server.quit()
