# Generated by Django 4.2.5 on 2023-12-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childvc', '0006_faqs_vid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Faqs',
        ),
    ]
