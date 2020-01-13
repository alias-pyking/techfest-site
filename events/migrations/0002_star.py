# Generated by Django 3.0.2 on 2020-01-12 16:32

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=events.models.upload_location)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]