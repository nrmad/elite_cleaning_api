from django.db import models
from django.contrib.postgres.fields import JSONField  # For PostgreSQL

from media.models import Media


class Sector(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.TextField()
    value = models.IntegerField()
    completed = models.DateField()
    contractor = models.TextField()
    description = models.TextField()
    sector = models.ForeignKey(Sector, related_name='projects', on_delete=models.CASCADE)
    media = models.ManyToManyField(Media, through='ProjectMedia')

    def __str__(self):
        return self.title

class ScopeOfWorks(models.Model):
    project = models.ForeignKey(Project, related_name='scope_of_works', on_delete=models.CASCADE)
    details = models.TextField()  # You can modify this to fit the structure of scope details

    def __str__(self):
        return f"Scope of Works for {self.project.title}"

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.project.title, self.media.description)