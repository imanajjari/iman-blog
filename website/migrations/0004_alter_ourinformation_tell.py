# Generated by Django 3.2.4 on 2023-07-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_ourinformation_tell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourinformation',
            name='tell',
            field=models.IntegerField(max_length=15),
        ),
    ]
