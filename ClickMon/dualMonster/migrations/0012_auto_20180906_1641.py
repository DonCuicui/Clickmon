# Generated by Django 2.1.1 on 2018-09-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dualMonster', '0011_auto_20180906_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickmon',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clickmon',
            name='stamina',
            field=models.IntegerField(default=0),
        ),
    ]
