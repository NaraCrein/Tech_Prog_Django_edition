# Generated by Django 4.0.4 on 2022-05-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avito', '0002_ad_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]