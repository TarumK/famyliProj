# Generated by Django 4.1.5 on 2023-01-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfamyli', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]