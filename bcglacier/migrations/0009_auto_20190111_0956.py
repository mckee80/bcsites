# Generated by Django 2.1.5 on 2019-01-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcglacier', '0008_auto_20190110_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
