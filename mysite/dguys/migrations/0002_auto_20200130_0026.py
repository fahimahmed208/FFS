# Generated by Django 2.2 on 2020-01-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dguy',
            name='location',
            field=models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Wari', 'Wari')], default='Farmgate', max_length=200),
        ),
        migrations.AddField(
            model_name='dguy',
            name='photo',
            field=models.ImageField(blank=True, default='store.gif', upload_to='propics'),
        ),
    ]
