# Generated by Django 4.2.5 on 2024-02-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childvc', '0012_alter_profile_address_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
