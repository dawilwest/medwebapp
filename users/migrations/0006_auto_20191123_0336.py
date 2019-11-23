# Generated by Django 2.2.7 on 2019-11-23 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191121_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalpractitioner',
            name='myuser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicalpractitioner_user', to=settings.AUTH_USER_MODEL, verbose_name='user name'),
        ),
        migrations.AlterField(
            model_name='sickuser',
            name='myuser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sickuser_user', to=settings.AUTH_USER_MODEL, verbose_name='user name'),
        ),
    ]