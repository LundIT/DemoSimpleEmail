from django.core.mail import send_mail
from django.db.models import BooleanField

import generic_app.models as models

class Email(models.UploadModelMixin):
    id = models.AutoField(primary_key=True)
    to_recipients = models.TextField()
    from_sender = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    approve_and_send = BooleanField()

    def update(self):
        if self.approve_and_send:
            send_mail(
                self.subject,
                self.message,
                self.from_sender,
                self.to_recipients.split(','),
                fail_silently=False,
            )
