# Generated by Django 2.1.5 on 2019-01-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcglacier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='area',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sites',
            name='code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sites',
            name='fires',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
