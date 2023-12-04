# Generated by Django 4.2.6 on 2023-11-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0009_alter_book_publication_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Luminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('course', models.CharField(max_length=30)),
            ],
        ),
    ]
