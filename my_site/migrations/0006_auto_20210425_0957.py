# Generated by Django 2.2.12 on 2021-04-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_about_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('link', models.URLField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
