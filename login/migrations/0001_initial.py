# Generated by Django 3.2.8 on 2021-10-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=8)),
                ('manager_passwd', models.CharField(max_length=20)),
                ('privilege', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'manager',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usersinfo',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=8)),
                ('user_passwd', models.CharField(max_length=20)),
                ('tel', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('credit_star', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usersinfo',
                'managed': True,
            },
        ),
    ]