# Generated by Django 2.0 on 2019-02-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_realisation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='niveau',
            field=models.IntegerField(default=0),
        ),
    ]