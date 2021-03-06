# Generated by Django 3.2.7 on 2021-09-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('bloodid', models.AutoField(db_column='bloodID', primary_key=True, serialize=False)),
                ('bloodtype', models.CharField(blank=True, db_column='bloodType', max_length=10, null=True)),
            ],
            options={
                'db_table': 'blood',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bloodbank',
            fields=[
                ('bankid', models.AutoField(db_column='bankID', primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('bankname', models.CharField(blank=True, db_column='bankName', max_length=20, null=True)),
            ],
            options={
                'db_table': 'bloodbank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donorid', models.AutoField(db_column='donorID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='phoneNumber', max_length=20, null=True)),
            ],
            options={
                'db_table': 'donor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.AutoField(db_column='hospitalID', primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('hospitalname', models.CharField(blank=True, db_column='hospitalName', max_length=20, null=True)),
            ],
            options={
                'db_table': 'hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientid', models.AutoField(db_column='patientID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('pbloodtype', models.CharField(blank=True, db_column='pBloodType', max_length=10, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('bankid', models.OneToOneField(db_column='bankID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='home.bloodbank')),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]
