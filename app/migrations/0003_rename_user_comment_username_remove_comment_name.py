# Generated by Django 4.0.1 on 2022-01-18 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment_email_comment_name_comment_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
