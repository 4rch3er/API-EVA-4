# Generated by Django 5.1.4 on 2024-12-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='estado',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='tipo_anime',
            field=models.CharField(max_length=100),
        ),
    ]