# Generated by Django 4.2.3 on 2023-07-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variavel', 'verbose_name_plural': 'Variacoes'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_curta',
            field=models.TextField(),
        ),
    ]
