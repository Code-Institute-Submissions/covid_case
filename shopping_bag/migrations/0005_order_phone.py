# Generated by Django 3.1.1 on 2020-10-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_bag', '0004_auto_20201005_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]