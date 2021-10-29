from django.db import models
import uuid 
# Create your models here.

class Chat(models.Model):
    # room_name = models.CharField(max_length=255)
    room_name = models.UUIDField(default=uuid.uuid4, editable=False)
    allowed_users = models.CharField(max_length=255)

    def __str__(self):
        return str(self.room_name)