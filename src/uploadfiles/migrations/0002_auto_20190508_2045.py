# Generated by Django 2.0.6 on 2019-05-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='document',
            field=models.ImageField(upload_to='staticfiles/img_hydraulics/'),
        ),
    ]