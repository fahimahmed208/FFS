# Generated by Django 2.2 on 2020-02-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguys', '0004_auto_20200130_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dguy',
            name='location',
            field=models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Wari', 'Wari'), ('Moghbazar', 'Moghbazar')], default='Farmgate', max_length=200),
        ),
    ]
