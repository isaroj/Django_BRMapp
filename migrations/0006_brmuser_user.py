# Generated by Django 3.0.6 on 2020-05-22 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BRMapp', '0005_auto_20200523_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='brmuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
