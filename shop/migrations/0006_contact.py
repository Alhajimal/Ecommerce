# Generated by Django 4.2.3 on 2023-10-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=500)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
