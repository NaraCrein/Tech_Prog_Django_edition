# Generated by Django 4.0.4 on 2022-05-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avito', '0004_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.FileField(default='image', upload_to=''),
        ),
    ]