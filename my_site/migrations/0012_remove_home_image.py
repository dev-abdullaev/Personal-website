# Generated by Django 3.2.8 on 2021-10-28 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0011_alter_home_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='image',
        ),
    ]