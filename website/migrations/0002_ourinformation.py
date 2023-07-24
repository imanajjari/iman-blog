# Generated by Django 3.2.4 on 2023-07-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('address_description', models.CharField(max_length=510)),
                ('tell', models.ImageField(upload_to='')),
                ('tell_description', models.CharField(max_length=510)),
                ('email', models.EmailField(max_length=254)),
                ('email_description', models.CharField(max_length=510)),
            ],
        ),
    ]