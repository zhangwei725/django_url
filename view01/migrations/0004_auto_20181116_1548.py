# Generated by Django 2.1.3 on 2018-11-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view01', '0003_auto_20181116_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girl',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
