# Generated by Django 3.0.11 on 2021-03-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('method', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('to_recipients', models.TextField()),
                ('from_sender', models.TextField()),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('approve_and_send', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserChangeLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('message', models.TextField()),
            ],
        ),
    ]
