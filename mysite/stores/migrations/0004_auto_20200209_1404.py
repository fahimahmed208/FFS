# Generated by Django 2.2 on 2020-02-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Wari', 'Wari'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Mohammadpur', 'Mohammadpur'), ('Uttara', 'Uttara'), ('Malibag', 'Malibag'), ('Khilgaon', 'Khilgaon'), ('Dhaka Cantonment', 'Dhaka Cantonment'), ('Jatrabari', 'Jatrabari'), ('Mouchak', 'Mouchak')], default='Farmgate', max_length=200),
        ),
    ]
