# Generated by Django 3.0.6 on 2020-05-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRMapp', '0004_auto_20200523_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='brmuser',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='brmuser',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
