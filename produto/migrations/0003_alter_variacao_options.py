# Generated by Django 4.2.3 on 2023-07-14 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variacao', 'verbose_name_plural': 'Variacoes'},
        ),
    ]