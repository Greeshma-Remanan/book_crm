# Generated by Django 4.2.6 on 2023-11-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0010_luminar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('hostel', models.CharField(max_length=30)),
            ],
        ),
    ]
