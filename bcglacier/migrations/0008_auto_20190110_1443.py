# Generated by Django 2.1.5 on 2019-01-10 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bcglacier', '0007_auto_20190110_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bcglacier.Parks'),
        ),
    ]