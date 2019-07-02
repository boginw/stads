from src.grade_printer import GradesPrinter

class GradesSender:
    fromEmail = None
    toEmail = None
    client = None

    def __init__(self, fromEmail, toEmail, client):
        self.fromEmail = fromEmail
        self.toEmail = toEmail
        self.client = client

    def send(self, grades):
        response = self.client.send_email(
            Source = self.fromEmail,
            Destination = { "ToAddresses": [ self.toEmail ] },
            Message = {
                "Subject": { "Data": "STADS: new grade!" },
                "Body": { "Html": { "Data": "<pre>" + GradesPrinter().print(grades).replace("\n", "<br />") + "</pre>" } }
            }
        )