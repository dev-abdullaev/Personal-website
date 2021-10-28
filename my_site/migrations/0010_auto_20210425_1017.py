# Generated by Django 2.2.12 on 2021-04-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0009_auto_20210425_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('link', models.URLField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
