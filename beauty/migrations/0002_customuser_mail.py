# Generated by Django 4.2.6 on 2023-11-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
