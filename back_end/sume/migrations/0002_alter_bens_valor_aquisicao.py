# Generated by Django 3.2.9 on 2021-12-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bens',
            name='valor_aquisicao',
            field=models.DecimalField(decimal_places=7, max_digits=12),
        ),
    ]
