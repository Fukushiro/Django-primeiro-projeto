# Generated by Django 3.1 on 2020-08-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_parametros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]