# Generated by Django 5.1.1 on 2024-09-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagen',
            field=models.ImageField(upload_to='static/portfolio/images'),
        ),
    ]
