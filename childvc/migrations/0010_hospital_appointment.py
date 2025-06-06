# Generated by Django 4.2.6 on 2023-12-27 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('childvc', '0009_faq_u_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=100)),
                ('haddress', models.TextField()),
                ('gmail', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('hid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childvc.hospital')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
