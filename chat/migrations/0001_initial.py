# Generated by Django 3.1.1 on 2021-10-29 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('allowed_users', models.CharField(max_length=255)),
            ],
        ),
    ]
