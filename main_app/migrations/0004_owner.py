# Generated by Django 4.2.3 on 2023-08-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_polish_cleaning_cleaning_alter_cleaning_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
            ],
        ),
    ]
