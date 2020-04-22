# Generated by Django 3.0.5 on 2020-04-21 20:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.City')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.Service')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
