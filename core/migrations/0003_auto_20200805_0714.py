# Generated by Django 3.0.3 on 2020-08-05 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200805_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
