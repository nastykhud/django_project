# Generated by Django 4.2.3 on 2023-07-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='info',
            field=models.CharField(default='Описание', max_length=1000),
            preserve_default=False,
        ),
    ]
