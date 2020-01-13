# Generated by Django 3.0.2 on 2020-01-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterEventUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('college_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]