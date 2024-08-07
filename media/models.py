from django.db import models

class Media(models.Model):

    url = models.URLField(max_length=2000)
    alt = models.TextField()
    cover_photo = models.BooleanField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description if self.description else 'Media Item'
