# Generated by Django 2.1.5 on 2019-01-08 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcglacier', '0004_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='site_id',
        ),
    ]