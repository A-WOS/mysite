# Generated by Django 3.1.3 on 2021-06-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='hits',
        ),
    ]