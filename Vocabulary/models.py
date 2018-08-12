from django.db import models
import uuid
# Create your models here.
class Vocab(models.Model):
    id  = models.UUIDField(unique=True, primary_key=True)
    word = models.CharField(max_length=33)
    meaning = models.TextField()

    def save(self, *args, **kwargs):
        self.id = uuid.uuid4()
        super(Vocab, self).save(*args, **kwargs)
