# Generated by Django 2.1.1 on 2018-09-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dualMonster', '0008_auto_20180906_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='stamina_cost',
            field=models.IntegerField(default=0),
        ),
    ]
