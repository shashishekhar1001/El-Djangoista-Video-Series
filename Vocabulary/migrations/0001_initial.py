# Generated by Django 2.0.7 on 2018-08-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('word', models.CharField(max_length=33)),
                ('meaning', models.TextField()),
            ],
        ),
    ]
