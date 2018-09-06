# Generated by Django 2.1.1 on 2018-09-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dualMonster', '0007_attack_stamina_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attack',
            name='exp',
        ),
        migrations.AddField(
            model_name='attackpack',
            name='exp_four',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attackpack',
            name='exp_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attackpack',
            name='exp_three',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attackpack',
            name='exp_two',
            field=models.IntegerField(default=0),
        ),
    ]
