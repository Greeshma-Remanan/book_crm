# Generated by Django 4.2.6 on 2023-12-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0011_marian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]
