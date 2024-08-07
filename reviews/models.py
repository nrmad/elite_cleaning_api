from django.db import models


class Review(models.Model):
    author = models.CharField(max_length=100)
    role = models.TextField()
    content = models.TextField()
    company = models.TextField()
    variant = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2} - {3} ".format(self.author, self.role, self.company, self.variant)