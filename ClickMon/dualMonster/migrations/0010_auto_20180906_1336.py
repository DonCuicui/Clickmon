# Generated by Django 2.1.1 on 2018-09-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dualMonster', '0009_auto_20180906_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickmon',
            name='summoner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clickmon', to='dualMonster.Summoner'),
        ),
    ]