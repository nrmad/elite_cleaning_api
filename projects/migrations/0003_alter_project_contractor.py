# Generated by Django 4.2.14 on 2024-10-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_completed_remove_project_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contractor',
            field=models.TextField(),
        ),
    ]