from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class LogRecord(models.Model):
    date_created = models.DateTimeField("date created", auto_now_add=True)
    comment = models.TextField(max_length=250)
    section = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log_records")
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.comment
