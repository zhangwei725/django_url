# Generated by Django 2.1.3 on 2018-11-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view01', '0004_auto_20181116_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girl',
            name='source',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
