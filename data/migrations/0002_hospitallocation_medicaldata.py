# Generated by Django 2.2.7 on 2019-11-21 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191120_1917'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(choices=[('Asthma', 'Asthma'), ('Sickle Cell Disease', 'Sickle Cell Disease'), ('Hypertension', 'Hypertension'), ('Allergies', 'Allergies'), ('Lung Disease', 'Lung Disease'), ('Others', 'Others')], max_length=200)),
                ('sickuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.SickUser')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(default='Abuja', max_length=200)),
                ('district', models.CharField(choices=[('Maitama', 'Maitama'), ('Garki', 'Garki'), ('Asokoro', 'Asokoro'), ('Wuse', 'Wuse'), ('Jabi', 'Jabi'), ('Karu', 'Karu')], max_length=200)),
                ('sickuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.SickUser')),
            ],
        ),
    ]
