# Generated by Django 3.1.1 on 2020-10-05 14:12

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201005_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], default='media/noimage.png', force_format=None, keep_meta=True, quality=0, size=[400, 500], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], default='media/noimage.png', force_format=None, keep_meta=True, quality=0, size=[400, 500], upload_to=''),
        ),
    ]
