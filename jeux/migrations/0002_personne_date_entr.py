# Generated by Django 3.2 on 2021-04-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='date_entr',
            field=models.DateField(null=True),
        ),
    ]
